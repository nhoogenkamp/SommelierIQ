// select fields to create number of fields https://stackoverflow.com/questions/73554956/how-to-display-fields-according-to-selected-input-using-plain-javascript

function genFields() {

    document.getElementById("fields").innerHTML = "";

    let numFields = document.getElementById("dishCount").value;

    for (let i = 1; i <= numFields; i++) {

        document.getElementById("fields").innerHTML += `

            <div>

                <label for="dish_${i}">Dish ${i}</label>

                <select id="dish_${i}" onchange="checkSauce(${i})">

                    <option value="">Select Dish</option>

                    <option value="Achill Island Oysters">
                        Achill Island Oysters
                    </option>

                    <option value="Pan Seared Scallops">
                        Pan Seared Scallops
                    </option>

                    <option value="Beetroot Carpaccio">
                        Beetroot Carpaccio
                    </option>

                    <option value="Short Rib Nugget">
                        Short Rib Nugget
                    </option>

                    <option value="Caesar Salad">Caesar Salad</option>

                    <option value="Chicken Liver & Foie Gras Parfait">
                        Chicken Liver & Foie Gras Parfait
                    </option>

                    <option value="Devilled Kidneys">Devilled Kidneys</option>

                    <option value="Dry Aged Beef Tartare">
                        Dry Aged Beef Tartare
                    </option>

                    <option value="F.X. Buckley Black Pudding Scotch Egg">
                        F.X. Buckley Black Pudding Scotch Egg
                    </option>

                    <option value="6oz Beef Fillet Medallions">
                        6oz Beef Fillet Medallions
                    </option>
                    
                    <option value="Fillet Steak">
                        Fillet Steak
                    </option>
                    
                    <option value="Rib Eye Steak">
                        Rib Eye Steak
                    </option>

                    <option value="Striploin Steak">
                        Striploin Steak
                    </option>

                    <option value="T-Bone Steak">
                        T-Bone Steak
                    </option>

                    <option value="Striploin on the Bone">
                        Striploin on the Bone
                    </option>

                    <option value="Ridgeway Wagyu Bone In Striploin">
                        Ridgeway Wagyu Bone In Striploin
                    </option>

                    <option value="Chateaubriand">
                        Chateaubriand
                    </option>

                    <option value="Irish Ex Dairy Cow Côte de Boeuf">
                        Irish Ex Dairy Cow Côte de Boeuf
                    </option>

                    <option value="Porterhouse Steak">
                        Porterhouse Steak
                    </option>

                    <option value="Braised Beef Cheek">
                        Braised Beef Cheek
                    </option>
                   
                    <option value="Free Range Chicken Roulade">
                        Free Range Chicken Roulade
                    </option>

                    <option value="Cornish Sole Meuniére">
                        Cornish Sole Meuniére
                    </option>


                </select>

                <div id="sauce_${i}"></div>

                <br><br>

            </div>

        `;
    }
}

function checkSauce(i) {

    let dish = document.getElementById(`dish_${i}`).value;

    if (
        dish == "Fillet Steak" ||
        dish == "Rib Eye Steak" ||
        dish == "Striploin Steak" ||
        dish == "Striploin on the Bone" ||
        dish == "Ridgeway Wagyu Bone In Striploin" ||
        dish == "T-Bone Steak"
    ) {

        document.getElementById(`sauce_${i}`).innerHTML = `
            
            <label>Sauce</label>

            <select>
                <option value="">Select Sauce</option>
                <option value="Pepper Sauce">Pepper Sauce</option>
                <option value="Bearnaise">Bearnaise</option>
                <option value="Garlic Butter">Garlic Butter</option>
                <option value="Bone Marrow Jus">Bone Marrow Jus</option>
                <option value="No Sauce">No Sauce</option>
            </select>

        `;

    } else {

        document.getElementById(`sauce_${i}`).innerHTML = "";

    }
}