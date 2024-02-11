
console.log('WIP')
const express = require('express');
const router = express.Router()

const allowedDomains = ['http://example.com', 'http://yourdomain.com'];

router.get('/login',function(req, res){
    let followPath = encodeURIComponent(req.query.path);
    let domain = 'http://example.com/';
    if(req.session.isAuthenticated()){
        if (allowedDomains.includes(domain)){
        res.redirect(domain+followPath); //false positive
        }
        else {
            res.redirect('/error');
        }
    }else{
        res.redirect('/');
    }
}); 

router.get('/goto', function(req, res) {
    if(req.session.isAuthenticated()) {
        let url = req.query.url;
        let domain = (new URL(url)).hostname;
        if (allowedDomains.includes(domain)) {
            res.redirect('/confirm-redirect');
        } else {
            res.redirect('/error');
        }
    } else {
        res.redirect('/');
    }
});

router.get('/confirm-redirect', function(req, res) {
    let url = req.query.url;
    res.render('confirm-redirect', { url: url });
});


module.exports = router
