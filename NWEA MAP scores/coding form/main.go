package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"
)

type Insight struct {
	Timestamp string `json:"timestamp"`
	Language  string `json:"language"`
	Rating    string `json:"rating"`
}

func handleInsight(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	if r.Method == "POST" {
		r.ParseForm()
		lang := r.FormValue("favorite_language")
		rating := r.FormValue("rating")
		
		f, _ := os.OpenFile("insights.csv", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		defer f.Close()
		
		writer := csv.NewWriter(f)
		writer.Write([]string{time.Now().Format("15:04:05"), lang, rating})
		writer.Flush()

		if r.Header.Get("X-Requested-With") == "XMLHttpRequest" {
			fmt.Fprintf(w, "Saved!")
		} else {
			http.Redirect(w, r, "/", http.StatusSeeOther)
		}
	}
}

func getInsights(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")

	f, err := os.Open("insights.csv")
	if err != nil {
		json.NewEncoder(w).Encode([]Insight{}) // Return empty list if file doesn't exist
		return
	}
	defer f.Close()

	rows, _ := csv.NewReader(f).ReadAll()
	var data []Insight
	for _, row := range rows {
		data = append(data, Insight{Timestamp: row[0], Language: row[1], Rating: row[2]})
	}
	json.NewEncoder(w).Encode(data)
}

func clearHistory(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	os.Remove("insights.csv") // Deletes the file
	fmt.Fprintf(w, "History Cleared")
}

func main() {
	http.HandleFunc("/submit", handleInsight)
	http.HandleFunc("/api/insights", getInsights)
	http.HandleFunc("/api/clear", clearHistory)
	fmt.Println("Server running at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
func main() {
    // Get the port from the environment (default to 8080 if not set)
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    http.HandleFunc("/submit", handleInsight)
    http.HandleFunc("/api/insights", getInsights)
    http.HandleFunc("/api/clear", clearHistory)

    fmt.Printf("Server starting on port %s...\n", port)
    http.ListenAndServe(":"+port, nil)
}
