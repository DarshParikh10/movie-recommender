function getRecommendations() {
    let movieName = document.getElementById("movieInput").value;
    
    fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ movie: movieName })
    })
    .then(response => response.json())
    .then(data => {
        let list = document.getElementById("recommendations");
        list.innerHTML = "";
        
        if (data.recommendations.length === 0) {
            list.innerHTML = "<li>No recommendations found</li>";
        } else {
            data.recommendations.forEach(movie => {
                let li = document.createElement("li");
                li.textContent = movie;
                list.appendChild(li);
            });
        }
    });
}
