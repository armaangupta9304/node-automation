const express = require('express');
const router = express.Router();
const controller = require('../controller/controller.js');

//* End Points *//
router.get('/', controller.getIndex);

module.exports = router;