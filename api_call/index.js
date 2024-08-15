const express = require('express');
const axios = require('axios');
const app = express();
const port = 8080;

// Obtener todos los productos
app.get('/products', async (req, res) => {
    try {
        const response = await axios.get('https://fakestoreapi.com/products');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch products', details: error.message });
    }
});

// Obtener un producto específico por ID
app.get('/products/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const response = await axios.get(`https://fakestoreapi.com/products/${id}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: `Failed to fetch product with ID ${id}`, details: error.message });
    }
});

// Obtener todas las categorías de productos
app.get('/categories', async (req, res) => {
    try {
        const response = await axios.get('https://fakestoreapi.com/products/categories');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch categories', details: error.message });
    }
});

// Obtener productos por categoría
app.get('/categories/:category/products', async (req, res) => {
    const { category } = req.params;
    try {
        const response = await axios.get(`https://fakestoreapi.com/products/category/${category}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: `Failed to fetch products for category ${category}`, details: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});