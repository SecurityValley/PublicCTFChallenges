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
    const pass = [106,117,115,116,95,119,97,114,109,105,110,103,95,117,112];
    const pa = Array.from(password);

    for(let i = 0; i < pa.length; i++) {
        if(pa[i].charCodeAt(0) !== pass[i]) {
            throw new Error("pass violation. wrong credentials");
        }
    }

    banner(password);
}

function banner(payload) {
    console.info("that was great !!!");
    console.info("run the following command to get the flag.")
    console.info(`curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{"pass": "${payload}"}'`)
}

