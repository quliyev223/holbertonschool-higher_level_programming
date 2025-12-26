// Write a JavaScript script that updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id "red_header".
//
// You must use document.querySelector
//
// Test with this HTML file:
//
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <title>Holberton School</title>
//   </head>
//   <body>
//     <header>
//       First HTML page
//     </header>
//     <div id="red_header">Red header</div>
//     <footer>
//       Holberton School - 2022
//     </footer>
//     <script type="text/javascript" src="1-script.js"></script>
//   </body>
// </html>

// Select the element with id "red_header" and add a click event listener
document.querySelector('#red_header').addEventListener('click', function () {
  // Change the text color of the <header> element to red
  document.querySelector('header').style.color = '#FF0000';
});
