document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("signupForm"); // Target form by ID for safety
    
    if (form) {
        form.addEventListener("submit", function (event) {
            // 1. FIXED: Select the correct name attributes from your HTML
            const password = document.querySelector("input[name='password']");
            const confirmPassword = document.querySelector("input[name='confirm_password']");

            // 2. Check if passwords match
            if (password && confirmPassword) {
                if (password.value !== confirmPassword.value) {
                    event.preventDefault(); // Stop form submission
                    alert("Passwords don't match. Please check them.");
                    confirmPassword.focus();
                    return; // Exit the function
                }
            }
            
            // Note: The 'required' attribute in HTML already handles empty field validation 
            // natively in the browser with nice tooltips. But if you still want JS to double-check:
            const requiredInputs = form.querySelectorAll("input[required]");
            for (let input of requiredInputs) {
                if (!input.value.trim()) {
                    event.preventDefault();
                    alert("Please fill all required fields.");
                    input.focus();
                    return;
                }
            }  
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const bookItems = document.querySelectorAll(".book-item");
    const noResultsMessage = document.getElementById("noResultsMessage");
    const clearSearchBtn = document.getElementById("clearSearchBtn");

    if (searchInput && bookItems.length > 0) {
        
        const filterBooks = function() {
            const term = searchInput.value.toLowerCase().trim();
            let visibleCount = 0;
            
            bookItems.forEach(item => {
                // Safely get text content from all searchable fields, fallback to empty string
                const title = item.querySelector(".book-title")?.textContent.toLowerCase() || "";
                const author = item.querySelector(".book-author")?.textContent.toLowerCase() || "";
                const category = item.querySelector(".book-category")?.textContent.toLowerCase() || "";
                const isbn = item.querySelector(".book-isbn")?.textContent.toLowerCase() || ""; // NEW: ISBN added

                // Check if term exists in title, author, category, OR isbn
                if (title.includes(term) || author.includes(term) || category.includes(term) || isbn.includes(term)) {
                    item.style.display = ""; // Show the item (resets to default CSS)
                    visibleCount++;
                } else {
                    item.style.display = "none"; // Hide the item
                }
            });

            // Show "No Results" message ONLY if visibleCount is 0 AND the user has typed something
            if (noResultsMessage) {
                if (visibleCount === 0 && term !== "") {
                    noResultsMessage.style.display = "block";
                } else {
                    noResultsMessage.style.display = "none";
                }
            }
        };

        // 1. Run filter whenever the user types
        searchInput.addEventListener("input", filterBooks);

        // 2. Clear search functionality
        if (clearSearchBtn) {
            clearSearchBtn.addEventListener("click", function() {
                searchInput.value = "";
                filterBooks(); // Reset the view to show all books
                searchInput.focus();
            });
        }
    }
});