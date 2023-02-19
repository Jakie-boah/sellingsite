document.addEventListener('DOMContentLoaded', function () {
            const SELECT_ID = '#sampleSelect'; // айдишник селекта

            const sampleSelect = document.querySelector(SELECT_ID);
            const inputs = document.querySelectorAll(`[data-select="${SELECT_ID}"]`)

            sampleSelect.addEventListener('change', function(e) {
                const optionValue = e.currentTarget.value; // Получаем выбранное значение


                inputs.forEach((input) => {
                    if (input.dataset.option === optionValue) {
                        input.removeAttribute('hidden')
                    } else {
                        input.setAttribute('hidden', '')
                    }
                })
            })
        });
        document.addEventListener('DOMContentLoaded', function () {
            const SELECT_ID = '#sampleSelect2'; // айдишник селекта

            const sampleSelect = document.querySelector(SELECT_ID);
            const inputs = document.querySelectorAll(`[data-select="${SELECT_ID}"]`)

            sampleSelect.addEventListener('change', function(e) {
                const optionValue = e.currentTarget.value; // Получаем выбранное значение


                inputs.forEach((input) => {
                    if (input.dataset.option === optionValue) {
                        input.removeAttribute('hidden')
                    } else {
                        input.setAttribute('hidden', '')
                    }
                })
            })
        });
        let birdForm = document.querySelectorAll(".images_row.bird-form")
        let container = document.querySelector("#form-container")
        let addButton = document.querySelector("#add-form")
        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

        let formNum = birdForm.length-1
        addButton.addEventListener('click', addForm)

        function addForm(e){
            e.preventDefault()
            console.log(birdForm)
            let newForm = birdForm[birdForm.length-1].cloneNode(true)
            let formRegex = RegExp(`form-(\\d){1}-`,'g')

            formNum++
            newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
            container.insertBefore(newForm, addButton)

            totalForms.setAttribute('value', `${formNum+1}`)
        }


        function showFile(input) {
          const file = input.files[0].name
          input.nextElementSibling.innerHTML = file
        };

        const regex = new RegExp('(\\d)()(?=(\\d{3})+(?!\\d))', 'g');

        function numberWithSpaces(e) {
            const x = e.target.value;
            e.target.value = x.replace(/\s/g, '').replace(regex, `$1 $2`);
        };

        const input = document.querySelectorAll('.price');
        input.forEach( inp => inp.addEventListener('input', numberWithSpaces));
        console.log(input);
//        input.addEventListener('input', numberWithSpaces);