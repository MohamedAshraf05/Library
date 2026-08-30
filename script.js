//validation
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function (event) {
            const password = document.querySelector("input[name='password1']") || document.querySelector("input[name='password']");
            const confirmPassword = document.querySelector("input[name='password2']");

            if (password && confirmPassword){
                if (password.value !== confirmPassword.value){
                    event.preventDefault();
                    alert("Passwords don't match, Please check them");
                    confirmPassword.focus();
                    return; 
                }
            }
            const requiredInputs = form.querySelectorAll("input[required]");
            for (let input of requiredInputs){
                if(!input.value.trim()){
                    event.preventDefault();
                    alert("Please fill all required fields");
                    input.focus();
                    return;
                }
            }  
        });
    }
});

//search  
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const bookItems = document.querySelectorAll(".book-item");

    if (searchInput){
        searchInput.addEventListener("input", function (e) {
            const term = e.target.value.toLowerCase().trim();
            bookItems.forEach(item=> {
                const title = item.querySelector(".book-title").textContent.toLowerCase();
                const author = item.querySelector(".book-author").textContent.toLowerCase();

                if (title.includes(term) || author.includes(term)) {
                    item.style.display ="";
                } else {
                    item.style.display = "none";
                }
            });
        });

    }
});