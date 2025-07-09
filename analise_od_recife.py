import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações para melhorar a visualização dos gráficos
plt.rcParams['figure.figsize'] = (12, 8)
plt.style.use('ggplot')
plt.rcParams['font.size'] = 12
sns.set(font_scale=1.2)

# Função para ler o arquivo CSV
def carregar_dados(arquivo):
    """
    Carrega os dados do arquivo CSV da pesquisa OD Recife 2016
    """
    try:
        # Leitura do arquivo com encoding UTF-8 e separador ponto e vírgula
        # Adicionando low_memory=False para evitar o aviso de tipos mistos
        df = pd.read_csv(arquivo, sep=';', encoding='utf-8', low_memory=False)
        print(f"Dados carregados com sucesso! Total de registros: {len(df)}")
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

# Função para limpar e preparar os dados
def preparar_dados(df):
    """
    Realiza a limpeza e preparação dos dados
    """
    # Renomeando colunas para facilitar o trabalho
    df_clean = df.copy()
    
    # Substituindo valores numéricos por categorias mais descritivas
    # Dicionário para sexo
    sexo_map = {1: 'Masculino', 2: 'Feminino'}
    if 'sexo' in df_clean.columns:
        df_clean['sexo_cat'] = df_clean['sexo'].map(sexo_map)
    
    # Dicionário para faixa etária
    faixa_etaria_map = {
        1: 'Até 6 anos',
        2: '6 a 15 anos',
        3: '16 a 24 anos',
        4: '25 a 39 anos',
        5: '40 a 59 anos',
        6: 'Acima de 60 anos'
    }
    if 'faixa_etaria' in df_clean.columns:
        df_clean['faixa_etaria_cat'] = df_clean['faixa_etaria'].map(faixa_etaria_map)
    
    # Dicionário para renda
    renda_map = {
        1: 'Até 1 SM',
        2: '1 a 2 SM',
        3: '2 a 3 SM',
        4: '3 a 5 SM',
        5: '5 a 10 SM',
        6: '10 a 20 SM',
        7: 'Mais de 20 SM',
        8: 'Sem rendimento',
        9: 'Sem declaração'
    }
    if 'renda' in df_clean.columns:
        df_clean['renda_cat'] = df_clean['renda'].map(renda_map)
    
    # Dicionário para mobilidade reduzida
    mobilidade_map = {0: 'Não declarado', 1: 'Sim', 2: 'Não'}
    if 'mobilidade_reduzida' in df_clean.columns:
        df_clean['mobilidade_reduzida_cat'] = df_clean['mobilidade_reduzida'].map(mobilidade_map)
    
    # Dicionário para meios de transporte
    transporte_map = {
        1: 'A pé',
        2: 'Bicicleta',
        3: 'Ônibus',
        4: 'Metrô',
        5: 'Carro (dirigindo)',
        6: 'Carro (carona familiar)',
        7: 'Carro (carona amigo)',
        8: 'Carro (motorista)',
        9: 'Motocicleta',
        10: 'Transporte escolar',
        11: 'Táxi',
        12: 'Fretado'
    }
    
    # Aplicando para transporte de trabalho e estudo
    # Nota: para valores compostos (múltiplas opções) mantém o valor original
    if 'meio_transporte_trab' in df_clean.columns:
        df_clean['transporte_trabalho_cat'] = df_clean['meio_transporte_trab'].apply(
            lambda x: transporte_map.get(x) if isinstance(x, (int, float)) and not pd.isna(x) and x in transporte_map else x
        )
    
    if 'transporte_aula' in df_clean.columns:
        df_clean['transporte_estudo_cat'] = df_clean['transporte_aula'].apply(
            lambda x: transporte_map.get(x) if isinstance(x, (int, float)) and not pd.isna(x) and x in transporte_map else x
        )
    
    return df_clean

# Função para analisar perfil demográfico
def analisar_demografia(df):
    """
    Realiza análise demográfica dos respondentes
    """
    print("\n===== ANÁLISE DEMOGRÁFICA =====")
    
    # Definindo os dicionários de mapeamento dentro da função
    # para resolver o problema de escopo
    faixa_etaria_map = {
        1: 'Até 6 anos',
        2: '6 a 15 anos',
        3: '16 a 24 anos',
        4: '25 a 39 anos',
        5: '40 a 59 anos',
        6: 'Acima de 60 anos'
    }
    
    renda_map = {
        1: 'Até 1 SM',
        2: '1 a 2 SM',
        3: '2 a 3 SM',
        4: '3 a 5 SM',
        5: '5 a 10 SM',
        6: '10 a 20 SM',
        7: 'Mais de 20 SM',
        8: 'Sem rendimento',
        9: 'Sem declaração'
    }
    
    # Distribuição por sexo
    if 'sexo_cat' in df.columns:
        print("\nDistribuição por Sexo:")
        sexo_count = df['sexo_cat'].value_counts()
        print(sexo_count)
        
        # Gráfico de distribuição por sexo
        plt.figure()
        sexo_count.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Distribuição por Sexo')
        plt.ylabel('')
        plt.savefig('distribuicao_sexo.png')
        plt.close()
    
    # Distribuição por faixa etária
    if 'faixa_etaria_cat' in df.columns:
        print("\nDistribuição por Faixa Etária:")
        faixa_count = df['faixa_etaria_cat'].value_counts().sort_index()
        print(faixa_count)
        
        # Gráfico de distribuição por faixa etária
        plt.figure()
        sns.countplot(data=df, x='faixa_etaria_cat', order=list(faixa_etaria_map.values()))
        plt.title('Distribuição por Faixa Etária')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('distribuicao_faixa_etaria.png')
        plt.close()
    
    # Distribuição por renda
    if 'renda_cat' in df.columns:
        print("\nDistribuição por Renda:")
        renda_count = df['renda_cat'].value_counts()
        print(renda_count)
        
        # Gráfico de distribuição por renda
        plt.figure()
        sns.countplot(data=df, x='renda_cat', order=[
            'Até 1 SM', '1 a 2 SM', '2 a 3 SM', '3 a 5 SM',
            '5 a 10 SM', '10 a 20 SM', 'Mais de 20 SM',
            'Sem rendimento', 'Sem declaração'
        ])
        plt.title('Distribuição por Renda (Salários Mínimos)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('distribuicao_renda.png')
        plt.close()

# Função para analisar mobilidade
def analisar_mobilidade(df):
    """
    Analisa os dados de mobilidade dos respondentes
    """
    print("\n===== ANÁLISE DE MOBILIDADE =====")
    
    # Pessoas com mobilidade reduzida
    if 'mobilidade_reduzida_cat' in df.columns:
        print("\nPessoas com Mobilidade Reduzida:")
        mobilidade_count = df['mobilidade_reduzida_cat'].value_counts()
        print(mobilidade_count)
        
        # Gráfico de mobilidade reduzida
        plt.figure()
        mobilidade_count.plot(kind='bar')
        plt.title('Pessoas com Mobilidade Reduzida')
        plt.tight_layout()
        plt.savefig('mobilidade_reduzida.png')
        plt.close()
    
    # Análise de pessoas que trabalham e estudam
    trabalham = df[df['trabalha'] == 1].shape[0]
    estudam = df[df['pesquisado_estuda'] == 1].shape[0]
    trabalham_estudam = df[(df['trabalha'] == 1) & (df['pesquisado_estuda'] == 1)].shape[0]
    
    print(f"\nPessoas que trabalham: {trabalham} ({trabalham/len(df)*100:.2f}%)")
    print(f"Pessoas que estudam: {estudam} ({estudam/len(df)*100:.2f}%)")
    print(f"Pessoas que trabalham e estudam: {trabalham_estudam} ({trabalham_estudam/len(df)*100:.2f}%)")
    
    # Gráfico de atividades
    atividades_data = {
        'Categoria': ['Trabalham', 'Estudam', 'Trabalham e estudam'],
        'Quantidade': [trabalham, estudam, trabalham_estudam]
    }
    atividades_df = pd.DataFrame(atividades_data)
    
    plt.figure()
    sns.barplot(data=atividades_df, x='Categoria', y='Quantidade')
    plt.title('Distribuição das Atividades')
    plt.tight_layout()
    plt.savefig('distribuicao_atividades.png')
    plt.close()

# Função para analisar meios de transporte
def analisar_transportes(df):
    """
    Analisa os meios de transporte utilizados
    """
    print("\n===== ANÁLISE DE TRANSPORTES =====")
    
    # Simplificando valores para meio_transporte_trab
    # Para fins de análise, consideramos apenas transportes únicos (não combinações)
    transportes_trab = {}
    
    for valor in df['meio_transporte_trab'].dropna().unique():
        if isinstance(valor, (int, float)) and valor in range(1, 13):
            if valor == 1:
                transportes_trab['A pé'] = len(df[df['meio_transporte_trab'] == 1])
            elif valor == 2:
                transportes_trab['Bicicleta'] = len(df[df['meio_transporte_trab'] == 2])
            elif valor == 3:
                transportes_trab['Ônibus'] = len(df[df['meio_transporte_trab'] == 3])
            elif valor == 4:
                transportes_trab['Metrô'] = len(df[df['meio_transporte_trab'] == 4])
            elif valor == 5:
                transportes_trab['Carro (dirigindo)'] = len(df[df['meio_transporte_trab'] == 5])
            elif valor == 6:
                transportes_trab['Carro (carona familiar)'] = len(df[df['meio_transporte_trab'] == 6])
            elif valor == 7:
                transportes_trab['Carro (carona amigo)'] = len(df[df['meio_transporte_trab'] == 7])
            elif valor == 8:
                transportes_trab['Carro (motorista)'] = len(df[df['meio_transporte_trab'] == 8])
            elif valor == 9:
                transportes_trab['Motocicleta'] = len(df[df['meio_transporte_trab'] == 9])
            elif valor == 10:
                transportes_trab['Transporte escolar'] = len(df[df['meio_transporte_trab'] == 10])
            elif valor == 11:
                transportes_trab['Táxi'] = len(df[df['meio_transporte_trab'] == 11])
            elif valor == 12:
                transportes_trab['Fretado'] = len(df[df['meio_transporte_trab'] == 12])
    
    # Fazendo o mesmo para transporte para estudo
    transportes_estudo = {}
    
    for valor in df['transporte_aula'].dropna().unique():
        if isinstance(valor, (int, float)) and valor in range(1, 13):
            if valor == 1:
                transportes_estudo['A pé'] = len(df[df['transporte_aula'] == 1])
            elif valor == 2:
                transportes_estudo['Bicicleta'] = len(df[df['transporte_aula'] == 2])
            elif valor == 3:
                transportes_estudo['Ônibus'] = len(df[df['transporte_aula'] == 3])
            elif valor == 4:
                transportes_estudo['Metrô'] = len(df[df['transporte_aula'] == 4])
            elif valor == 5:
                transportes_estudo['Carro (dirigindo)'] = len(df[df['transporte_aula'] == 5])
            elif valor == 6:
                transportes_estudo['Carro (carona familiar)'] = len(df[df['transporte_aula'] == 6])
            elif valor == 7:
                transportes_estudo['Carro (carona amigo)'] = len(df[df['transporte_aula'] == 7])
            elif valor == 8:
                transportes_estudo['Carro (motorista)'] = len(df[df['transporte_aula'] == 8])
            elif valor == 9:
                transportes_estudo['Motocicleta'] = len(df[df['transporte_aula'] == 9])
            elif valor == 10:
                transportes_estudo['Transporte escolar'] = len(df[df['transporte_aula'] == 10])
            elif valor == 11:
                transportes_estudo['Táxi'] = len(df[df['transporte_aula'] == 11])
            elif valor == 12:
                transportes_estudo['Fretado'] = len(df[df['transporte_aula'] == 12])
    
    # Exibindo resultados
    print("\nMeios de Transporte para o Trabalho:")
    for modo, quantidade in sorted(transportes_trab.items(), key=lambda x: x[1], reverse=True):
        print(f"{modo}: {quantidade} ({quantidade/trabalham*100:.2f}%)")
    
    print("\nMeios de Transporte para Estudo:")
    for modo, quantidade in sorted(transportes_estudo.items(), key=lambda x: x[1], reverse=True):
        print(f"{modo}: {quantidade} ({quantidade/estudam*100:.2f}%)")
    
    # Criando dataframes para visualização
    transportes_trab_df = pd.DataFrame({
        'Meio': list(transportes_trab.keys()),
        'Quantidade': list(transportes_trab.values())
    }).sort_values('Quantidade', ascending=False)
    
    transportes_estudo_df = pd.DataFrame({
        'Meio': list(transportes_estudo.keys()),
        'Quantidade': list(transportes_estudo.values())
    }).sort_values('Quantidade', ascending=False)
    
    # Gráfico para meios de transporte para trabalho
    plt.figure(figsize=(14, 8))
    sns.barplot(data=transportes_trab_df, x='Meio', y='Quantidade')
    plt.title('Meios de Transporte para o Trabalho')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('transportes_trabalho.png')
    plt.close()
    
    # Gráfico para meios de transporte para estudo
    plt.figure(figsize=(14, 8))
    sns.barplot(data=transportes_estudo_df, x='Meio', y='Quantidade')
    plt.title('Meios de Transporte para Estudo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('transportes_estudo.png')
    plt.close()

# Função para analisar uso de aplicativos de táxi e terminais de integração
def analisar_tecnologia(df):
    """
    Analisa o uso de tecnologia (aplicativos) e terminais de integração
    """
    print("\n===== ANÁLISE DE TECNOLOGIA E INTEGRAÇÃO =====")
    
    # Uso de internet no celular
    if 'internet_celular' in df.columns:
        internet_celular = df['internet_celular'].value_counts()
        total_respondentes = internet_celular.sum()
        
        # Calculando a porcentagem de pessoas com celular e internet
        tem_internet = internet_celular.get(1, 0)
        percentual_internet = (tem_internet / total_respondentes) * 100
        
        print(f"\nPessoas com celular e acesso à internet: {tem_internet} ({percentual_internet:.2f}%)")
    
    # Uso de aplicativos para táxi (trabalho)
    taxi_trabalho = {}
    if 'utiliza_app_taxi_trabalho' in df.columns:
        for valor in [1, 2, 3]:  # 1-Nunca, 2-Às vezes, 3-Sempre
            taxi_trabalho[valor] = len(df[(df['meio_transporte_trab'] == 11) & (df['utiliza_app_taxi_trabalho'] == valor)])
        
        total_taxi_trabalho = sum(taxi_trabalho.values())
        
        if total_taxi_trabalho > 0:
            print("\nUso de aplicativos para táxi (trabalho):")
            print(f"Nunca: {taxi_trabalho.get(1, 0)} ({taxi_trabalho.get(1, 0)/total_taxi_trabalho*100:.2f}% dos usuários de táxi)")
            print(f"Às vezes: {taxi_trabalho.get(2, 0)} ({taxi_trabalho.get(2, 0)/total_taxi_trabalho*100:.2f}% dos usuários de táxi)")
            print(f"Sempre: {taxi_trabalho.get(3, 0)} ({taxi_trabalho.get(3, 0)/total_taxi_trabalho*100:.2f}% dos usuários de táxi)")
    
    # Uso de terminais de integração
    terminal_trabalho = {}
    if 'utiliza_terminal_int_trabalho' in df.columns:
        for valor in [0, 1, 2]:  # 0-Não declarado, 1-Sim, 2-Não
            terminal_trabalho[valor] = len(df[(df['meio_transporte_trab'] == 3) & (df['utiliza_terminal_int_trabalho'] == valor)])
        
        total_onibus_trabalho = len(df[df['meio_transporte_trab'] == 3])
        
        if total_onibus_trabalho > 0:
            print("\nUso de terminais de integração (trabalho):")
            print(f"Sim: {terminal_trabalho.get(1, 0)} ({terminal_trabalho.get(1, 0)/total_onibus_trabalho*100:.2f}% dos usuários de ônibus)")
            print(f"Não: {terminal_trabalho.get(2, 0)} ({terminal_trabalho.get(2, 0)/total_onibus_trabalho*100:.2f}% dos usuários de ônibus)")
            print(f"Não declarado: {terminal_trabalho.get(0, 0)} ({terminal_trabalho.get(0, 0)/total_onibus_trabalho*100:.2f}% dos usuários de ônibus)")
    
    # Uso de aplicativos para táxi (estudo)
    taxi_estudo = {}
    if 'utiliza_app_taxi_aula' in df.columns:
        for valor in [1, 2, 3]:  # 1-Nunca, 2-Às vezes, 3-Sempre
            taxi_estudo[valor] = len(df[(df['transporte_aula'] == 11) & (df['utiliza_app_taxi_aula'] == valor)])
        
        total_taxi_estudo = sum(taxi_estudo.values())
        
        if total_taxi_estudo > 0:
            print("\nUso de aplicativos para táxi (estudo):")
            print(f"Nunca: {taxi_estudo.get(1, 0)} ({taxi_estudo.get(1, 0)/total_taxi_estudo*100:.2f}% dos usuários de táxi)")
            print(f"Às vezes: {taxi_estudo.get(2, 0)} ({taxi_estudo.get(2, 0)/total_taxi_estudo*100:.2f}% dos usuários de táxi)")
            print(f"Sempre: {taxi_estudo.get(3, 0)} ({taxi_estudo.get(3, 0)/total_taxi_estudo*100:.2f}% dos usuários de táxi)")

# Função principal que executa toda a análise
def analisar_pesquisa_od(arquivo_csv):
    """
    Função principal que realiza toda a análise da pesquisa OD Recife 2016
    """
    # Carrega os dados
    df = carregar_dados(arquivo_csv)
    
    if df is None:
        print("Não foi possível realizar a análise devido a erros na leitura do arquivo.")
        return
    
    # Informações básicas sobre o dataset
    print("\n===== INFORMAÇÕES BÁSICAS =====")
    print(f"Número de registros: {len(df)}")
    print(f"Colunas disponíveis: {', '.join(df.columns)}")
    
    # Preparar dados
    df_clean = preparar_dados(df)
    
    # Variáveis globais para uso em outras funções
    global trabalham, estudam
    trabalham = df[df['trabalha'] == 1].shape[0]
    estudam = df[df['pesquisado_estuda'] == 1].shape[0]
    
    # Executar análises
    analisar_demografia(df_clean)
    analisar_mobilidade(df_clean)
    analisar_transportes(df_clean)
    analisar_tecnologia(df_clean)
    
    print("\n===== ANÁLISE CONCLUÍDA =====")
    print("Os gráficos foram salvos no diretório atual.")

# Para executar a análise, basta chamar a função principal
if __name__ == "__main__":
    # Substitua pelo caminho correto do arquivo CSV
    arquivo_csv = "pesquisaodrecife2016.csv"
    analisar_pesquisa_od(arquivo_csv)