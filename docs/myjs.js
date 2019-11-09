function classify(a, b, c) {
        if (isNaN(a)) {
            return "Első nem szám";
        }
        if (isNaN(b)) {
            return "Második nem szám";
        }
        if (isNaN(c)) {
            return "Harmadik nem szám";
        }

        a_number=parseInt(a);
        b_number=parseInt(b);
        c_number=parseInt(c);

        if (a <= 0 || b <= 0 || c <= 0) return "Negatív";
        if (a == b && b == c) return "Egyenlő oldalú";
        if (a_number >= b_number+c_number || parseInt(c) >= b_number+a_number || parseInt(b) >= a_number+c_number) return "Nem háromszög";
        if (b==c || a==b || a==c) return "Egyenlő szárú";
        return "Általános";
}

window.onload = function() {
    document.getElementById("calculate-button").onclick = function() {
        let a = document.getElementById("a-input").value;
        let b = document.getElementById("b-input").value;
        let c = document.getElementById("c-input").value;

        let result = document.getElementById("result-ul");

        result.innerHTML += "<li>" + "a = " + a + ", b = " + b + ", c = " + c + ": " + classify(a, b, c) + "</li>";
        return false;
    }
};