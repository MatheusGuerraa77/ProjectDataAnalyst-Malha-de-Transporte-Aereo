# ✈️ **Malha de Transporte Aéreo: Otimização de Rotas Aéreas**

## **📋 Descrição Geral**
Este projeto foi desenvolvido com o objetivo de **modelar e otimizar a malha de transporte aéreo**, utilizando a teoria dos grafos para representar:  
- **Aeroportos**: nós do grafo.  
- **Rotas aéreas**: arestas ponderadas com base em critérios como distância, tempo de voo, custo ou consumo de combustível.  

O modelo permite **análises estruturadas** da malha aérea, oferecendo soluções escaláveis e práticas para problemas reais.

---

## **🎯 Objetivos Alcançados**
- 🗺️ **Modelagem de Grafos**  
  Representação dos aeroportos e rotas aéreas como um **grafo ponderado**, baseando-se em métricas ajustáveis para diferentes análises.  
- ⚙️ **Algoritmos de Busca**  
  - **Dijkstra**: Para encontrar a **rota mais curta** entre dois aeroportos.  
  - **A***: Para determinar a **rota de menor custo**, considerando critérios mais complexos.  
- 🔄 **Escalabilidade**  
  Suporte para grandes conjuntos de aeroportos e rotas, permitindo aplicação em redes extensas e densas.

---

## **🔗 Aplicações**
### 🚀 **Planejamento Estratégico**
- Identificação de **rotas mais econômicas e eficientes**, contribuindo para a **redução de custos operacionais** em companhias aéreas.
  
### 📊 **Gestão de Fluxos Aéreos**
- Otimização de **redirecionamentos e atrasos**.  
- Planejamento adaptativo para redes aéreas complexas.

### 📈 **Análises Operacionais**
- Ferramenta para tomadas de decisão no planejamento de voos diários, especialmente em rotas densas ou congestionadas.

---

## **💻 Tecnologias Utilizadas**
- **Python**: Linguagem base para implementação.  
  - 📦 **NetworkX**: Modelagem e manipulação de grafos.  
  - 🌍 **Geopy**: Cálculo das distâncias geográficas entre aeroportos.  
  - 📊 **Matplotlib**: Visualização da malha aérea com gráficos interativos.  
  - 🌟 **Streamlit**: Interface amigável e interativa para simulação de rotas, permitindo que usuários explorem as opções de otimização.

---

## **📌 Destaques Interativos**
### **1️⃣ Interface Visual (Streamlit)**  
Uma interface intuitiva e fácil de usar para:  
- **Explorar a malha aérea:** Visualização gráfica dos aeroportos e rotas.  
- **Simular rotas:** Teste em tempo real dos algoritmos (Dijkstra e A*).  

### **2️⃣ Gráficos e Visualizações**  
- **Mapa de rotas:** Representação clara e precisa da malha aérea.  
- **Comparação de algoritmos:** Visualizações interativas para comparar custos e distâncias.

---

## **🌟 Impacto e Aplicabilidade**
Este projeto apresenta um sistema robusto para o planejamento e otimização de rotas aéreas, com aplicações em:  
- **Empresas aéreas:** Redução de custos e otimização operacional.  
- **Logística de transporte:** Planejamento eficiente de rotas de carga.  
- **Academia:** Base para estudos avançados em grafos e transporte aéreo.  

### **🚀 Próximos Passos**
- Adicionar **previsão de condições climáticas** na análise das rotas.  
- Integrar dados reais de tráfego aéreo para testes em cenários reais.
