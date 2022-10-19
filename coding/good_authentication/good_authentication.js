const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Please enter password \n', password => {
    console.log(`Gonna check if ${password} is correct`);
    readline.close();
    validate(password)
});

function validate(password) {

    if (password.length != 12) {
        throw new Error("pass violation. wrong password length");
    }


    const block1 = Array.from(password).slice(0, 4)
    const block2 = Array.from(password).slice(4, 8)
    const block3 = Array.from(password).slice(8, 12)

    const block = [
        block1,
        block2,
        block3
    ]

    let crafted = "";

    for (let i = 0; i < block.length; i++) {
        for (let a = 0; a < block[i].length; a++) {
            if (i == 0) {
                crafted += String.fromCharCode(String(block[i][a]).charCodeAt(0) ^ 7)
            } else if (i == 1) {
                crafted += String.fromCharCode(String(block[i][a]).charCodeAt(0) ^ 11)
            } else {
                crafted += String.fromCharCode(String(block[i][a]).charCodeAt(0) ^ 9)
            }
        }
    }

    if(crafted !== "sontTbxTjffe") {
        throw new Error("pass violation. wrong credentials");
    }


    banner(password);
}

function banner(payload) {
    console.info("that was great !!!");
    console.info("run the following command to get the flag.")
    console.info(`curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{"pass": "${payload}"}'`)
}


