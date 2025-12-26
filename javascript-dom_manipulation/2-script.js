// Write a JavaScript script that adds the class "red" to the <header> element
// when the user clicks on the tag with id "red_header".
//
// You must use document.querySelector and classList.add()
//
// Test with this HTML file:
//
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <title>Holberton School</title>
//     <style>
//       .red {
//         color: #FF0000;
//       }
//     </style>
//   </head>
//   <body>
//     <header>
//       First HTML page
//     </header>
//     <div id="red_header">Red header</div>
//     <footer>
//       Holberton School - 2022
//     </footer>
//     <script type="text/javascript" src="2-script.js"></script>
//   </body>
// </html>

// Select the element with id "red_header" and add a click event listener
document.querySelector('#red_header').addEventListener('click', function () {
  // Add the "red" class to the <header> element
  document.querySelector('header').classList.add('red');
});
