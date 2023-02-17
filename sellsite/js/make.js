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
        };


        function showFile(input) {
          const file = input.files[0].name
          input.nextElementSibling.innerHTML = file
        };

        function numberWithSpaces(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        };

        const input = document.querySelector('.price');
        input.addEventListener('input', numberWithSpaces)