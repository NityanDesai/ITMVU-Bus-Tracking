// let submit = document.getElementById('submit');
// submit.addEventListener('click', (e) => {
//     if (document.getElementById('npassw').value != document.getElementById('con_passw').value) {
//         e.preventDefault();
//         document.getElementById('message').innerHTML = `<div style="font-size: smaller; color: red;" class=" card-subtitle mb-2" id='message'>Must be same as new password.</div>`
//     }
// });

// let form = document.getElementById('form');

// form.onsubmit = submit1;

// function submit1(e) {
//     e.preventDefault();
//     let success = document.getElementById('success');
//     success.innerHTML = `<div class="alert alert-success alert-dismissible fade show" role="alert">
//                             <strong>Well done!</strong> You just changed your password.
//                             <button id="close" type="button" class="close" data-dismiss="alert" aria-label="Close">
//                                 <span aria-hidden="true">&times;</span>
//                             </button>
//                         </div>`;
//     let close = document.getElementById('close');
//     close.addEventListener('click', () => {
//         location.reload();
//     })
// }

// // TODO: Add failiure alert if old password doesn't match with stored DB password.
