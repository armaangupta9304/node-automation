//* Import Statements *//
const express = require('express');
const routes = require('./routes/routes');
const app = express()
let port = process.env.PORT || 3000;

//* App Configs *//
app.use(express.json());
app.use('/api', routes);
app.use((req, res, next) => {
    res.status(404).json({
        message: "Invalid End Point",
        _err = 404
    })
})

//* Listening On Correct Port *//
app.listen(port, () => {
    console.log(`Server Up And Listening On Port: ${port}`);
})