// function updateQuantity(operation,productId)
// {

//    const inputBox= document.getElementById("quantity"+productId);
//    inputBox.value=parseInt(inputBox.value)+operation;

// }

function updateQuantity(operation,productId)
{
   const inputBox= document.getElementById("quantity "+productId);
   inputBox.value=parseInt(inputBox.value)+operation;

   if (inputBox.value < 0) {

      inputBox.value = 0
   }

   if (inputBox.value > 12) {

      inputBox.value = 12
   }
}