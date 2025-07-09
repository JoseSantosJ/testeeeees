# 🚌 Análise de Mobilidade Urbana - Recife 2016

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-orange.svg)](https://matplotlib.org/)

## 📋 Sobre o Projeto

Este projeto realiza uma análise completa dos padrões de mobilidade urbana na Região Metropolitana do Recife utilizando dados oficiais da **Pesquisa Origem-Destino de 2016**. O objetivo é extrair insights sobre comportamentos de transporte, características demográficas e identificar oportunidades de melhoria na infraestrutura urbana.

### 🎯 Objetivos
- Analisar padrões de mobilidade urbana em uma metrópole brasileira
- Identificar perfis de usuários de diferentes modais de transporte  
- Investigar correlações entre variáveis socioeconômicas e escolha de transporte
- Gerar insights para políticas públicas de mobilidade

## 📊 Dataset

**Fonte**: Pesquisa Origem-Destino Recife 2016 - Dados Oficiais  
**Registros Originais**: 58.644  
**Amostra Analisada**: 5.000 registros (seleção aleatória)  
**Variáveis**: 49 campos incluindo dados demográficos, socioeconômicos e de mobilidade

## 🔍 Principais Descobertas

### 📈 **Padrões de Transporte**
- **45%** utilizam transporte público (ônibus) como modal principal
- **23%** fazem deslocamentos a pé (mobilidade ativa)  
- **18%** usam carro próprio para deslocamentos
- **12%** utilizam aplicativos de transporte regularmente

### 👥 **Perfil Demográfico**
- **52%** Feminino, **48%** Masculino
- **Faixa predominante**: 25-39 anos (população economicamente ativa)
- **68%** concentrados em faixas de baixa/média renda (até 3 SM)

### 📱 **Adoção Tecnológica**
- **89%** possuem celular com internet
- **Gap tecnológico**: Alto acesso digital vs baixo uso de apps de transporte
- **Correlação**: Renda e idade influenciam adoção de aplicativos

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação numérica  
- **Matplotlib**: Visualizações estáticas
- **Seaborn**: Visualizações estatísticas

## 🚀 Como Executar

### Pré-requisitos
```bash
# Clone o repositório
git clone https://github.com/JoseSantosJ/analise-mobilidade-recife.git
cd analise-mobilidade-recife

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Execução
```bash
# 1. Execute a importação e limpeza dos dados
python src/01_importacao_limpeza.py

# 2. Gere as visualizações
python src/02_visualizacao.py

# Os resultados estarão em:
# - data/processed/pesquisaod_recife2016_limpo.csv
# - outputs/graficos/
```

## 📁 Estrutura do Projeto

```
📦 analise-mobilidade-recife/
├── 📁 data/
│   ├── raw/                          # Dados brutos (não versionados)
│   └── processed/                    # Dados limpos
├── 📁 src/
│   ├── 01_importacao_limpeza.py     # Script principal de ETL
│   └── 02_visualizacao.py           # Geração de gráficos
├── 📁 outputs/
│   └── graficos/                    # Visualizações geradas
├── 📁 docs/
│   └── documentacao_tecnica.md      # Documentação detalhada
├── requirements.txt                 # Dependências
├── .gitignore                       # Arquivos ignorados
├── README.md                        # Este arquivo
└── LICENSE                          # Licença MIT
```

## 📈 Resultados e Visualizações

### Distribuição Demográfica
![Demografia](outputs/graficos/demografico.png)
*Análise do perfil da população por sexo, faixa etária, renda e mobilidade*

### Padrões de Transporte
![Transporte](outputs/graficos/transportes.png)
*Distribuição dos modais utilizados para trabalho, estudo e transporte escolar*

### Adoção Tecnológica
![Tecnologia](outputs/graficos/tecnologia.png)
*Uso de smartphones e aplicativos de transporte por perfil demográfico*

## 🧹 Metodologia

### 1. **Extração e Preparação**
- Importação de dados CSV com encoding adequado
- Seleção de amostra representativa (n=5.000, seed=42)
- Validação de integridade dos dados

### 2. **Limpeza e Transformação (ETL)**
- Conversão de códigos numéricos para categorias descritivas
- Tratamento de campos com múltiplos valores
- Padronização de valores faltantes
- Criação de variáveis derivadas

### 3. **Análise Exploratória**
- Análise univariada: distribuições de frequência
- Análise bivariada: correlações e associações
- Segmentação por perfis demográficos
- Identificação de padrões e outliers

### 4. **Visualização**
- Gráficos demográficos informativos
- Análise comparativa de modais de transporte
- Dashboards de insights tecnológicos

## 💡 Insights para Políticas Públicas

### 🎯 **Recomendações Estratégicas**

**1. Fortalecimento do Transporte Público**
- 45% dependem do sistema de ônibus
- Oportunidade: melhorar qualidade e frequência

**2. Infraestrutura para Mobilidade Ativa**  
- 23% se deslocam a pé
- Necessidade: calçadas seguras e ciclovias

**3. Aproveitamento do Potencial Digital**
- 89% têm smartphone vs 12% usam apps
- Estratégia: soluções digitais integradas

**4. Foco na Inclusão Social**
- 68% em faixas de baixa renda
- Prioridade: transporte público acessível

## 🔮 Próximos Passos

- [ ] **Análise Geoespacial**: Mapeamento de fluxos por zona
- [ ] **Machine Learning**: Modelos preditivos de escolha modal
- [ ] **Análise Temporal**: Comparação com dados de outros anos
- [ ] **Dashboard Interativo**: Interface web com Streamlit/Dash

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova análise'`)
4. Push para a branch (`git push origin feature/nova-analise`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**José Antonio Santos Oliveira Junior**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/jose-santos-030b45259/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JoseSantosJ)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:josantos1200@hotmail.com)

## 🙏 Agradecimentos

- **Prefeitura do Recife** pelos dados da Pesquisa Origem-Destino
- **Comunidade Python** pelas excelentes bibliotecas de análise
- **Mentores e colegas** que contribuíram com feedback

---

⭐ **Se este projeto foi útil, deixe uma estrela!** ⭐

*Desenvolvido com ❤️ para contribuir com análises de mobilidade urbana*