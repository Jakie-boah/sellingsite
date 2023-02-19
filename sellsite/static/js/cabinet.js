document.addEventListener("DOMContentLoaded", function() {
            btn1.addEventListener('click', function (event) {
                event.preventDefault();
                div1.hidden = !div1.hidden;
                div2.hidden = true;
                div3.hidden = true;
            })

            btn2.addEventListener('click', function (event) {
                event.preventDefault();
                div2.hidden = !div2.hidden;
                div1.hidden = true;
                div3.hidden = true;
            })

            btn3.addEventListener('click', function (event) {
                event.preventDefault();
                div3.hidden = !div3.hidden;
                div1.hidden = true;
                div2.hidden = true;
            })
        });