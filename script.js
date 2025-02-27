document.addEventListener("DOMContentLoaded", function() {
    console.log("TrashSync Loaded");

    // 🚀 Schedule Pickup Form
    document.getElementById("pickupForm").addEventListener("submit", function(event) {
        event.preventDefault();
        let user = document.getElementById("user").value;
        let location = document.getElementById("location").value;
        let date = document.getElementById("date").value;

        fetch("/schedule", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: user, location: location, date: date })
        }).then(response => response.json())
          .then(data => {
              alert(data.message);
              fetchPickups();  // Refresh pickup list
          });
    });

    // 🚀 Report Uncollected Trash
    document.getElementById("reportForm").addEventListener("submit", function(event) {
        event.preventDefault();
        let pickupId = document.getElementById("pickupId").value;

        fetch("/report", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: pickupId })
        }).then(response => response.json())
          .then(data => {
              alert(data.message);
              fetchPickups();  // Refresh pickup list
          });
    });

    // 🚀 Fetch Scheduled Pickups
    function fetchPickups() {
        fetch("/pickups")
        .then(response => response.json())
        .then(data => {
            let pickupList = document.getElementById("pickupList");
            pickupList.innerHTML = "";
            data.forEach(pickup => {
                let li = document.createElement("li");
                li.textContent = `Pickup ID: ${pickup[0]} | ${pickup[1]} - ${pickup[2]} on ${pickup[3]} | Status: ${pickup[4]}`;
                pickupList.appendChild(li);
            });
        });
    }

    fetchPickups();  // Load pickups on page load
});
