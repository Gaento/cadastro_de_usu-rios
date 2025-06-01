# 🧑‍💻 Sistema de Gerenciamento de Usuários

Este é um sistema de gerenciamento de usuários desenvolvido em Python com persistência de dados utilizando **MySQL**. Ele permite cadastrar, listar, atualizar e excluir usuários diretamente pelo terminal.

---

## ⚙️ Funcionalidades

- ✅ Cadastro de novos usuários
- ✅ Validação de email e telefone
- ✅ Listagem de todos os usuários
- ✅ Atualização de nome, email ou telefone
- ✅ Exclusão de usuários
- ✅ Persistência de dados via MySQL

---

## 🛠️ Tecnologias

- Python 3
- MySQL
- Biblioteca `mysql-connector-python`
- Expressões Regulares (`re`)

---

## 💾 Estrutura esperada da tabela `users` no MySQL

Antes de executar, crie o banco de dados `user_system` e a tabela `users` com:

```sql
CREATE DATABASE user_system;

USE user_system;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    telephone VARCHAR(20)
);
