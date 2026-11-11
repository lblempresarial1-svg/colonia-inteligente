
# Colônia Inteligente
### Sistema Integrado de Gerenciamento de Energia

## 1. Sobre o projeto

O Colônia Inteligente é um sistema desenvolvido em Python para simular o gerenciamento de energia de uma colônia.

O sistema organiza informações, toma decisões automáticas, realiza previsões de geração eólica e analisa o consumo energético.

## 2. Funcionalidades

- Organização de dados utilizando listas e dicionários.
- Representação hierárquica dos subsistemas energéticos.
- Decisões automáticas por meio de estruturas condicionais.
- Previsão de geração eólica utilizando regressão linear simples.
- Análise de geração, consumo e reserva de energia.

## 3. Tecnologias utilizadas

- Python 3
- Funções
- Listas e dicionários
- Estruturas condicionais
- Regressão linear simples

Não são necessárias bibliotecas externas.

## 4. Organização dos arquivos

| Arquivo | Função |
|---|---|
| main.py | Menu principal e integração |
| dados.py | Armazenamento dos dados |
| decisoes.py | Regras de decisão |
| previsao.py | Previsão de energia |
| analise_energia.py | Análise energética |

## 5. Como executar

1. Instale o Python 3.
2. Baixe ou clone o repositório.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

```bash
python main.py
```

## 6. Exemplos de entrada e saída

### Previsão de energia

Entrada:
- Velocidade do vento: 11

Saída:
- Previsão de geração eólica: 27.5

### Análise energética

Entrada:
- Geração: 45
- Consumo: 60

Saída:
- ALERTA: consumo maior que geração.

## 7. Objetivo acadêmico

Demonstrar a aplicação de estruturas de dados, lógica de programação, regressão linear e análise energética em um sistema integrado.

## 8. Considerações finais

O sistema busca auxiliar o gerenciamento energético da colônia, identificando situações de risco, estimando a geração futura e sugerindo o armazenamento de energia excedente.

---

Projeto acadêmico desenvolvido em 2026.
