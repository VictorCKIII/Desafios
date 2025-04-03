<template>
  <div id="app">
    <header>
      <h1>Consulta de Operadoras de Saúde</h1>
    </header>
    <main>
      <div class="search-container">
        <input 
          type="text" 
          v-model="searchTerm" 
          placeholder="Digite o nome da operadora..."
          @keyup.enter="searchOperadoras"
        />
        <button @click="searchOperadoras">Buscar</button>
      </div>
      
      <div v-if="loading" class="loading">Carregando...</div>
      <div v-if="error" class="error">{{ error }}</div>
      
      <div v-if="results.length > 0" class="results">
        <div v-for="(item, index) in results" :key="index" class="result-item">
          <h3>{{ item.Nome_Fantasia || 'Sem nome fantasia' }}</h3>
          <p>{{ item.Razao_Social }}</p>
        </div>
      </div>
      <div v-else-if="!loading && searchPerformed" class="no-results">
        Nenhum resultado encontrado.
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      searchTerm: '',
      results: [],
      loading: false,
      error: null,
      searchPerformed: false
    }
  },
  methods: {
    async searchOperadoras() {
      if (!this.searchTerm.trim()) return;
      
      this.loading = true;
      this.error = null;
      this.searchPerformed = true;
      
      try {
        const response = await fetch(`/api/buscar?q=${encodeURIComponent(this.searchTerm)}`);
        
        if (!response.ok) {
          throw new Error('Erro na requisição');
        }
        
        const rawData = await response.json();
        console.log('Dados recebidos:', rawData);
        
        // Atualiza os resultados diretamente no array 'results'
        this.results = Array.isArray(rawData) 
          ? rawData.map(item => ({
              Razao_Social: item.Razao_Social || 'Não informado',
              Nome_Fantasia: item.Nome_Fantasia || item.Razao_Social || 'Sem nome fantasia'
            }))
          : [];
          
      } catch (error) {
        console.error('Erro:', error);
        this.error = 'Ocorreu um erro ao buscar os dados';
        this.results = [];
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  color: #2c3e50;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

header h1 {
  color: #3498db;
  font-weight: 600;
}

.search-container {
  display: flex;
  gap: 10px;
  margin-bottom: 2rem;
}

.search-container input {
  flex-grow: 1;
  padding: 12px 15px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  transition: all 0.3s ease;
  outline: none;
}

.search-container input:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
}

.search-container button {
  padding: 12px 24px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-container button:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
}

.search-container button:active {
  transform: translateY(0);
}

.loading, .error, .no-results {
  padding: 15px;
  text-align: center;
  border-radius: 8px;
  margin: 1rem 0;
}

.loading {
  background-color: #f8f9fa;
  color: #7f8c8d;
}

.error {
  background-color: #fdecea;
  color: #e74c3c;
}

.no-results {
  background-color: #f8f9fa;
  color: #7f8c8d;
}

.results {
  margin-top: 2rem;
  display: grid;
  gap: 1rem;
}

.result-item {
  padding: 1.5rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.result-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.result-item h3 {
  color: #3498db;
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.result-item p {
  color: #7f8c8d;
  margin: 0;
}

@media (max-width: 600px) {
  .search-container {
    flex-direction: column;
  }
  
  .search-container button {
    width: 100%;
  }
}
</style>

