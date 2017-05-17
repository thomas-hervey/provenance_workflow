'use strict'

import gulp from 'gulp';
import uglify from 'gulp-uglify';
import browserSync from 'browser-sync';

const reload = browserSync.reload;
const exec = require('child_process').exec;

//Run Flask server
gulp.task('runserver', function() {
    const proc = exec('python run.py');
});

// Default task: Watch Files For Changes & Reload browser
gulp.task('default', ['runserver'], function () {
  browserSync({
    notify: false,
    proxy: "127.0.0.1:3005"
  });

  gulp.watch(['app/*/templates/*.*', '*.py', 'app/*.py', 'app/*/*.py'], reload);
});