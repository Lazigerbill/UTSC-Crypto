function changecolor() {
    if (document.getElementById("percent_change").charAt(0) === '-') {
        document.getElementById("percent_change").className = "text-warning";
        document.getElementById("percent_change").className = "fa fa-level-down";
    }
}