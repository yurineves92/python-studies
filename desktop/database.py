import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="todo.db"):
        """Inicializa a conexão com o banco de dados"""
        self.db_name = db_name
        self.criar_tabela()
    
    def conectar(self):
        """Cria conexão com o banco de dados"""
        return sqlite3.connect(self.db_name)
    
    def criar_tabela(self):
        """Cria a tabela de tarefas se não existir"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT DEFAULT 'Pendente',
                prioridade TEXT DEFAULT 'Normal',
                data_criacao TEXT NOT NULL,
                data_conclusao TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def adicionar_tarefa(self, titulo, descricao, prioridade="Normal"):
        """Adiciona uma nova tarefa"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, prioridade, data_criacao)
            VALUES (?, ?, ?, ?)
        ''', (titulo, descricao, prioridade, data_criacao))
        
        conn.commit()
        conn.close()
        return True
    
    def listar_tarefas(self, filtro_status=None):
        """Lista todas as tarefas ou filtra por status"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        if filtro_status:
            cursor.execute('SELECT * FROM tarefas WHERE status = ? ORDER BY id DESC', (filtro_status,))
        else:
            cursor.execute('SELECT * FROM tarefas ORDER BY id DESC')
        
        tarefas = cursor.fetchall()
        conn.close()
        return tarefas
    
    def buscar_tarefa(self, tarefa_id):
        """Busca uma tarefa específica por ID"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tarefas WHERE id = ?', (tarefa_id,))
        tarefa = cursor.fetchone()
        
        conn.close()
        return tarefa
    
    def atualizar_tarefa(self, tarefa_id, titulo, descricao, prioridade):
        """Atualiza os dados de uma tarefa"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tarefas 
            SET titulo = ?, descricao = ?, prioridade = ?
            WHERE id = ?
        ''', (titulo, descricao, prioridade, tarefa_id))
        
        conn.commit()
        conn.close()
        return True
    
    def marcar_concluida(self, tarefa_id):
        """Marca uma tarefa como concluída"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            UPDATE tarefas 
            SET status = 'Concluída', data_conclusao = ?
            WHERE id = ?
        ''', (data_conclusao, tarefa_id))
        
        conn.commit()
        conn.close()
        return True
    
    def marcar_pendente(self, tarefa_id):
        """Marca uma tarefa como pendente"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tarefas 
            SET status = 'Pendente', data_conclusao = NULL
            WHERE id = ?
        ''', (tarefa_id,))
        
        conn.commit()
        conn.close()
        return True
    
    def excluir_tarefa(self, tarefa_id):
        """Exclui uma tarefa"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
        
        conn.commit()
        conn.close()
        return True
    
    def contar_tarefas(self):
        """Retorna estatísticas das tarefas"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM tarefas')
        total = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "Pendente"')
        pendentes = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "Concluída"')
        concluidas = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total': total,
            'pendentes': pendentes,
            'concluidas': concluidas
        }