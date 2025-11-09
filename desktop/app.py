import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class TodoApp:
    def __init__(self, root):
        """Inicializa a aplicação"""
        self.root = root
        self.root.title("Sistema de Tarefas - To-Do List")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Inicializar banco de dados
        self.db = Database()
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Criar interface
        self.criar_widgets()
        
        # Carregar tarefas
        self.carregar_tarefas()
        
        # Atualizar estatísticas
        self.atualizar_estatisticas()
    
    def configurar_estilo(self):
        """Configura o estilo da aplicação"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores
        self.cor_primaria = "#2c3e50"
        self.cor_secundaria = "#3498db"
        self.cor_sucesso = "#27ae60"
        self.cor_perigo = "#e74c3c"
        self.cor_fundo = "#ecf0f1"
    
    def criar_widgets(self):
        """Cria todos os widgets da interface"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = tk.Label(
            main_frame, 
            text="📝 Sistema de Tarefas", 
            font=("Arial", 24, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_primaria
        )
        titulo.pack(pady=10)
        
        # Frame de estatísticas
        self.criar_frame_estatisticas(main_frame)
        
        # Frame de formulário
        self.criar_frame_formulario(main_frame)
        
        # Frame de lista de tarefas
        self.criar_frame_lista(main_frame)
        
        # Frame de botões de ação
        self.criar_frame_acoes(main_frame)
    
    def criar_frame_estatisticas(self, parent):
        """Cria o frame de estatísticas"""
        stats_frame = tk.Frame(parent, bg=self.cor_fundo)
        stats_frame.pack(fill=tk.X, pady=10)
        
        # Total
        self.label_total = tk.Label(
            stats_frame,
            text="Total: 0",
            font=("Arial", 12),
            bg=self.cor_primaria,
            fg="white",
            padx=20,
            pady=10
        )
        self.label_total.pack(side=tk.LEFT, padx=5)
        
        # Pendentes
        self.label_pendentes = tk.Label(
            stats_frame,
            text="Pendentes: 0",
            font=("Arial", 12),
            bg=self.cor_secundaria,
            fg="white",
            padx=20,
            pady=10
        )
        self.label_pendentes.pack(side=tk.LEFT, padx=5)
        
        # Concluídas
        self.label_concluidas = tk.Label(
            stats_frame,
            text="Concluídas: 0",
            font=("Arial", 12),
            bg=self.cor_sucesso,
            fg="white",
            padx=20,
            pady=10
        )
        self.label_concluidas.pack(side=tk.LEFT, padx=5)
    
    def criar_frame_formulario(self, parent):
        """Cria o frame do formulário de nova tarefa"""
        form_frame = tk.LabelFrame(
            parent,
            text="Nova Tarefa",
            font=("Arial", 12, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_primaria,
            padx=10,
            pady=10
        )
        form_frame.pack(fill=tk.X, pady=10)
        
        # Título
        tk.Label(form_frame, text="Título:", bg=self.cor_fundo).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_titulo = tk.Entry(form_frame, width=40, font=("Arial", 10))
        self.entry_titulo.grid(row=0, column=1, pady=5, padx=5)
        
        # Descrição
        tk.Label(form_frame, text="Descrição:", bg=self.cor_fundo).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_descricao = tk.Entry(form_frame, width=40, font=("Arial", 10))
        self.entry_descricao.grid(row=1, column=1, pady=5, padx=5)
        
        # Prioridade
        tk.Label(form_frame, text="Prioridade:", bg=self.cor_fundo).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.combo_prioridade = ttk.Combobox(
            form_frame,
            values=["Baixa", "Normal", "Alta", "Urgente"],
            state="readonly",
            width=37
        )
        self.combo_prioridade.set("Normal")
        self.combo_prioridade.grid(row=2, column=1, pady=5, padx=5)
        
        # Botão adicionar
        btn_adicionar = tk.Button(
            form_frame,
            text="➕ Adicionar Tarefa",
            command=self.adicionar_tarefa,
            bg=self.cor_sucesso,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=20,
            pady=5
        )
        btn_adicionar.grid(row=3, column=0, columnspan=2, pady=10)
    
    def criar_frame_lista(self, parent):
        """Cria o frame da lista de tarefas"""
        lista_frame = tk.LabelFrame(
            parent,
            text="Lista de Tarefas",
            font=("Arial", 12, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_primaria,
            padx=10,
            pady=10
        )
        lista_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Filtro
        filtro_frame = tk.Frame(lista_frame, bg=self.cor_fundo)
        filtro_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(filtro_frame, text="Filtrar:", bg=self.cor_fundo).pack(side=tk.LEFT, padx=5)
        
        self.combo_filtro = ttk.Combobox(
            filtro_frame,
            values=["Todas", "Pendente", "Concluída"],
            state="readonly",
            width=15
        )
        self.combo_filtro.set("Todas")
        self.combo_filtro.pack(side=tk.LEFT, padx=5)
        self.combo_filtro.bind("<<ComboboxSelected>>", lambda e: self.carregar_tarefas())
        
        # Treeview
        tree_frame = tk.Frame(lista_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Criar Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Título", "Descrição", "Status", "Prioridade", "Data"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Descrição", text="Descrição")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Prioridade", text="Prioridade")
        self.tree.heading("Data", text="Data Criação")
        
        self.tree.column("ID", width=50)
        self.tree.column("Título", width=150)
        self.tree.column("Descrição", width=200)
        self.tree.column("Status", width=100)
        self.tree.column("Prioridade", width=100)
        self.tree.column("Data", width=150)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Bind duplo clique
        self.tree.bind("<Double-1>", self.editar_tarefa)
    
    def criar_frame_acoes(self, parent):
        """Cria o frame de botões de ação"""
        acoes_frame = tk.Frame(parent, bg=self.cor_fundo)
        acoes_frame.pack(fill=tk.X, pady=10)
        
        # Botão Concluir
        btn_concluir = tk.Button(
            acoes_frame,
            text="✓ Marcar Concluída",
            command=self.marcar_concluida,
            bg=self.cor_sucesso,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_concluir.pack(side=tk.LEFT, padx=5)
        
        # Botão Pendente
        btn_pendente = tk.Button(
            acoes_frame,
            text="↻ Marcar Pendente",
            command=self.marcar_pendente,
            bg=self.cor_secundaria,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_pendente.pack(side=tk.LEFT, padx=5)
        
        # Botão Excluir
        btn_excluir = tk.Button(
            acoes_frame,
            text="🗑 Excluir",
            command=self.excluir_tarefa,
            bg=self.cor_perigo,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_excluir.pack(side=tk.LEFT, padx=5)
        
        # Botão Atualizar
        btn_atualizar = tk.Button(
            acoes_frame,
            text="🔄 Atualizar",
            command=self.carregar_tarefas,
            bg=self.cor_primaria,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_atualizar.pack(side=tk.RIGHT, padx=5)
    
    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa"""
        titulo = self.entry_titulo.get().strip()
        descricao = self.entry_descricao.get().strip()
        prioridade = self.combo_prioridade.get()
        
        if not titulo:
            messagebox.showwarning("Atenção", "O título é obrigatório!")
            return
        
        try:
            self.db.adicionar_tarefa(titulo, descricao, prioridade)
            messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
            
            # Limpar campos
            self.entry_titulo.delete(0, tk.END)
            self.entry_descricao.delete(0, tk.END)
            self.combo_prioridade.set("Normal")
            
            # Atualizar lista
            self.carregar_tarefas()
            self.atualizar_estatisticas()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar tarefa: {str(e)}")
    
    def carregar_tarefas(self):
        """Carrega as tarefas na lista"""
        # Limpar lista
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obter filtro
        filtro = self.combo_filtro.get()
        filtro_status = None if filtro == "Todas" else filtro
        
        # Carregar tarefas
        tarefas = self.db.listar_tarefas(filtro_status)
        
        for tarefa in tarefas:
            self.tree.insert("", tk.END, values=tarefa[:6])
        
        # Atualizar estatísticas
        self.atualizar_estatisticas()
    
    def atualizar_estatisticas(self):
        """Atualiza as estatísticas"""
        stats = self.db.contar_tarefas()
        
        self.label_total.config(text=f"Total: {stats['total']}")
        self.label_pendentes.config(text=f"Pendentes: {stats['pendentes']}")
        self.label_concluidas.config(text=f"Concluídas: {stats['concluidas']}")
    
    def marcar_concluida(self):
        """Marca a tarefa selecionada como concluída"""
        selecionado = self.tree.selection()
        
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma tarefa!")
            return
        
        item = self.tree.item(selecionado[0])
        tarefa_id = item['values'][0]
        
        try:
            self.db.marcar_concluida(tarefa_id)
            messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")
            self.carregar_tarefas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar tarefa: {str(e)}")
    
    def marcar_pendente(self):
        """Marca a tarefa selecionada como pendente"""
        selecionado = self.tree.selection()
        
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma tarefa!")
            return
        
        item = self.tree.item(selecionado[0])
        tarefa_id = item['values'][0]
        
        try:
            self.db.marcar_pendente(tarefa_id)
            messagebox.showinfo("Sucesso", "Tarefa marcada como pendente!")
            self.carregar_tarefas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar tarefa: {str(e)}")
    
    def excluir_tarefa(self):
        """Exclui a tarefa selecionada"""
        selecionado = self.tree.selection()
        
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma tarefa!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente excluir esta tarefa?")
        
        if resposta:
            item = self.tree.item(selecionado[0])
            tarefa_id = item['values'][0]
            
            try:
                self.db.excluir_tarefa(tarefa_id)
                messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
                self.carregar_tarefas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir tarefa: {str(e)}")
    
    def editar_tarefa(self, event):
        """Abre janela para editar tarefa (duplo clique)"""
        selecionado = self.tree.selection()
        
        if not selecionado:
            return
        
        item = self.tree.item(selecionado[0])
        tarefa_id = item['values'][0]
        
        # Buscar tarefa completa
        tarefa = self.db.buscar_tarefa(tarefa_id)
        
        if not tarefa:
            return
        
        # Criar janela de edição
        self.criar_janela_edicao(tarefa)
    
    def criar_janela_edicao(self, tarefa):
        """Cria janela para editar tarefa"""
        janela = tk.Toplevel(self.root)
        janela.title("Editar Tarefa")
        janela.geometry("400x250")
        janela.resizable(False, False)
        
        # Título
        tk.Label(janela, text="Título:", font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        entry_titulo = tk.Entry(janela, width=30, font=("Arial", 10))
        entry_titulo.insert(0, tarefa[1])
        entry_titulo.grid(row=0, column=1, padx=10, pady=10)
        
        # Descrição
        tk.Label(janela, text="Descrição:", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        entry_descricao = tk.Entry(janela, width=30, font=("Arial", 10))
        entry_descricao.insert(0, tarefa[2] if tarefa[2] else "")
        entry_descricao.grid(row=1, column=1, padx=10, pady=10)
        
        # Prioridade
        tk.Label(janela, text="Prioridade:", font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        combo_prioridade = ttk.Combobox(
            janela,
            values=["Baixa", "Normal", "Alta", "Urgente"],
            state="readonly",
            width=27
        )
        combo_prioridade.set(tarefa[4])
        combo_prioridade.grid(row=2, column=1, padx=10, pady=10)
        
        # Botão salvar
        def salvar():
            titulo = entry_titulo.get().strip()
            descricao = entry_descricao.get().strip()
            prioridade = combo_prioridade.get()
            
            if not titulo:
                messagebox.showwarning("Atenção", "O título é obrigatório!")
                return
            
            try:
                self.db.atualizar_tarefa(tarefa[0], titulo, descricao, prioridade)
                messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
                janela.destroy()
                self.carregar_tarefas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar tarefa: {str(e)}")
        
        btn_salvar = tk.Button(
            janela,
            text="💾 Salvar",
            command=salvar,
            bg=self.cor_sucesso,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=20,
            pady=5
        )
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=20)