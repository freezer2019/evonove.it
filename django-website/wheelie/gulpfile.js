require('gulp');

// importing Wheelie instance and a list of tasks (recipe)
var wheelie = require('wheelie');
var recipe = require('wheelie-recipe');

// adding a recipe to Wheelie, defining the default task
wheelie.add(recipe);
wheelie.setDefault('watch');

// build customizations
var vendors = [
    'jquery/dist/jquery.js',
    'particles.js/particles.js',
    'svg-injector/svg-injector.js',
    'three.js/build/three.js',
    'three.js/examples/js/SimplexNoise.js',
    'threex.terrain/threex.terrain.js'
];

var scripts = [
    'mouse-pixels.js',
    'people.js',
    'projects-pixelation.js',
    'scroll-down.js',
    'svg-injections.js',
    'blog-tags.js',
    'texture3d.js',
    'viewport.js'
];

wheelie.update('uglify', {
  scripts: scripts,
  vendors: vendors
});

wheelie.setBuild('static/');
wheelie.setDist('static/');
wheelie.build();
