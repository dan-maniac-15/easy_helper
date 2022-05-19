function getAddress(url, postal, prefecture_J, prefecture_E, city_J, city_E, street1_J, street1_E){
    retvalue = null;
    const request = new XMLHttpRequest();
    request.open("get", url, true);
    request.send();
    request.onload = function(){
        const address_texts = request.responseText;
        inputAddress(address_texts, postal, prefecture_J, prefecture_E, city_J, city_E, street1_J, street1_E);
    }
}

function inputAddress(address_texts, postal, prefecture_J, prefecture_E, city_J, city_E, street1_J, street1_E){
    v_prefecture_J = "";
    v_prefecture_E = "";
    v_city_J       = "";
    v_city_E       = "";
    v_street1_J    = "";
    v_street1_E    = "";
    address_list = address_texts.split("\n");
    for(var i = 0; i < address_list.length; ++i){
        address = address_list[i].split(",")
        address_postal = address[0];
    
        if(address_postal.trim() == postal.trim()){
            v_prefecture_J = address[1];
            v_prefecture_E = address[4];
            v_city_J       = address[2];
            v_city_E       = address[5];
            v_street1_J    = address[3];
            v_street1_E    = address[6];
            if(v_street1_J.trim() == "以下に掲載がない場合"){
                v_street1_J = "";
            }
            else if(v_street1_J.indexOf("（")){
                v_street1_J = v_street1_J.split("（")[0];
            }
            if(v_street1_E.trim() == "IKANIKEISAIGANAIBAAI"){
                v_street1_E = "";
            }
            else if(v_street1_E.indexOf("(")){
                v_street1_E = v_street1_E.split("(")[0];
            }
        }
    }
    document.getElementById(prefecture_J).value = v_prefecture_J;            
    document.getElementById(prefecture_E).value = v_prefecture_E;            
    document.getElementById(city_J).value       = v_city_J;           
    document.getElementById(city_E).value       = v_city_E;           
    document.getElementById(street1_J).value    = v_street1_J;
    document.getElementById(street1_E).value    = v_street1_E;
}
