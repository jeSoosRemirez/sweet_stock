// Define the FastAPI base URL
const API_URL = 'http://localhost:8000';

// Create Product Form Submission
document.getElementById('create-product-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;
    const description = document.getElementById('description').value;

    const productData = {
        name: name,
        price: parseFloat(price),
        description: description
    };

    try {
        const response = await fetch(`${API_URL}/products/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productData),
        });

        if (response.ok) {
            const product = await response.json();
            alert(`Product created: ${product.name}`);
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        console.error('Error creating product:', error);
        alert('Failed to create product.');
    }
});

// Get Product by ID
document.getElementById('get-product-btn').addEventListener('click', async function() {
    const productId = document.getElementById('product-id').value;
    if (!productId) {
        alert('Please enter a product ID');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/products/${productId}`);
        const product = await response.json();

        if (response.ok) {
            document.getElementById('product-info').innerHTML = `
                <strong>Product Details:</strong><br>
                Name: ${product.name}<br>
                Price: $${product.price}<br>
                Description: ${product.description}
            `;
        } else {
            document.getElementById('product-info').innerHTML = `Error: ${product.detail}`;
        }
    } catch (error) {
        console.error('Error fetching product:', error);
        document.getElementById('product-info').innerHTML = 'Failed to retrieve product.';
    }
});

function openTab(evt, modelName) {
    // Hide all tab content
    const tabContents = document.querySelectorAll(".tabcontent");
    tabContents.forEach(content => content.style.display = "none");

    // Remove the "active" class from all buttons
    const tabLinks = document.querySelectorAll(".tablink");
    tabLinks.forEach(link => link.classList.remove("active"));

    // Show the current tab and add an "active" class to the button
    document.getElementById(modelName).style.display = "block";
    evt.currentTarget.classList.add("active");
}

// Fetch the list of products and display them
async function fetchProductList() {
    const response = await fetch('/products/');
    const data = await response.json();
    const productListDiv = document.getElementById('product-list');
    productListDiv.innerHTML = data.map(product => `<div>${product.name} - ${product.price}</div>`).join('');
}

// Call fetch functions on page load
window.onload = function () {
    fetchProductList();
    // Repeat the above for each model (Provider, Storage, etc.)
};
