function calculateSubtotal(){
    // Obtén todos los elementos que tengan un ID que comience con 'id_details-' y termine con '-price'
    const priceFields = document.querySelectorAll('[id^="id_details-"][id$="-price"]');
    const quantityFields = document.querySelectorAll('[id^="id_details-"][id$="-quantity"]');
    const productFields = document.querySelectorAll('[id^="id_details-"][id$="-product"]');
 
    // Función para actualizar el subtotal
    function updateSubtotal(quantityField, priceField, subtotalField) {
        const quantity = parseInt(quantityField.value, 10);
        const price = parseFloat(priceField.value);
        const subtotal = quantity * price;
        subtotalField.value = subtotal.toFixed(2);
        subtotalField.readOnly = true;
    }

    productFields.forEach(function (productField) {
        productField.addEventListener('change', function () {
            console.log("Se elegio un producto");
        });
    });
 
    // Agregar eventos 'input' a los campos de cantidad y precio
    priceFields.forEach(function (priceField) {
        const priceFieldID = priceField.id;
        const quantityFieldID = priceFieldID.replace('-price', '-quantity');
        const subtotalFieldID = priceFieldID.replace('-price', '-subtotal');
 
        const quantityField = document.querySelector('#' + quantityFieldID);
        const subtotalField = document.querySelector('#' + subtotalFieldID);
 
        priceField.addEventListener('input', function () {
            updateSubtotal(quantityField, priceField, subtotalField);
        });
    });
 
    quantityFields.forEach(function (quantityField) {
        const quantityFieldID = quantityField.id;
        const priceFieldID = quantityFieldID.replace('-quantity', '-price');
        const subtotalFieldID = quantityFieldID.replace('-quantity', '-subtotal');
 
        const priceField = document.querySelector('#' + priceFieldID);
        const subtotalField = document.querySelector('#' + subtotalFieldID);
 
        quantityField.addEventListener('input', function () {
            updateSubtotal(quantityField, priceField, subtotalField);
        });
    });
 }

document.addEventListener('DOMContentLoaded', function () {
    calculateSubtotal();
});

document.addEventListener('formset:added', (event) => {
    calculateSubtotal();
});

document.addEventListener('formset:removed', (event) => {
    console.log("Se quito una fila")
});