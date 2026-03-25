const dataFile = "insights.json"

// Helper to save current history to the file
func saveToFile() {
    data, _ := json.MarshalIndent(history, "", "  ")
    os.WriteFile(dataFile, data, 0644)
}

// Helper to load history from the file on startup
func loadFromFile() {
    data, err := os.ReadFile(dataFile)
    if err == nil {
        json.Unmarshal(data, &history)
    }
}


func main() {
	func main() {
		loadFromFile() // Load existing data first!

		port := os.Getenv("PORT")
		if port == "" { 
			port = "8080" 
		}

		http.Handle("/", http.FileServer(http.Dir(".")))
		http.HandleFunc("/submit", handleInsight)
		http.HandleFunc("/api/insights", getInsights)
		http.HandleFunc("/api/clear", clearHistory)

		fmt.Printf("Server starting on port %s... 🐹\n", port)
		http.ListenAndServe(":"+port, nil)
		}	

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    // THIS IS THE KEY! It maps your folder to the web browser
    http.Handle("/", http.FileServer(http.Dir(".")))

    http.HandleFunc("/submit", handleInsight)
    http.HandleFunc("/api/insights", getInsights)
    http.HandleFunc("/api/clear", clearHistory)

    fmt.Printf("Server starting on port %s...\n", port)
    http.ListenAndServe(":"+port, nil)

	var (
	history []Insight
	lock    sync.RWMutex
	)

	type Insight struct {
		Timestamp string `json:"timestamp"`
		Language  string `json:"language"`
		Rating    string `json:"rating"`
	}

	func handleInsight(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost { return }

		lock.Lock()
		defer lock.Unlock()

		history = append(history, Insight{
			Timestamp: time.Now().Format("03:04 PM"),
			Language:  r.FormValue("favorite_language"),
			Rating:    r.FormValue("rating"),
		})
		
		// Redirect back to home or send 200 OK
		w.WriteHeader(http.StatusOK)
	}

	func getInsights(w http.ResponseWriter, r *http.Request) {
		lock.RLock()
		defer lock.RUnlock()
		
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(history)
	}

	func clearHistory(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		
		history = []Insight{}
		w.WriteHeader(http.StatusOK)
	}

}
