function RunSentimentAnalysis() {
    const text = document.getElementById('textToAnalyze').value;
    if (!text) {
        document.getElementById('system_response').innerText = 'Please enter text to analyze.';
        return;
    }


    // Using query string as in the provided Flask route
    const url = '/sentimentAnalyzer?textToAnalyze=' + encodeURIComponent(text);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('system_response').innerText = 'Error: ' + (data.detail || data.error);
            } else {
                document.getElementById('system_response').innerText = 'The given text has been identified as ' + data.label + ' with a score of ' + data.score + '.';
            }
        })
        .catch(err => {
            document.getElementById('system_response').innerText = 'Request failed: ' + err;
        });
}