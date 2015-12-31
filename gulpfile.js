var gulp   = require('gulp');
var watch  = require('gulp-watch');
var sass   = require('gulp-sass');
var nano   = require('gulp-cssnano');
var rename = require("gulp-rename");

gulp.task('sass', function() {
    gulp.src('./static/css/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./static/css'));
});

gulp.task('minify', function () {
    gulp.src('./static/css/main.css')
        .pipe(nano())
        .pipe(rename('main.min.css'))
        .pipe(gulp.dest('./static/css/'))
});

gulp.task('build',function() {
    gulp.run('sass');
    gulp.run('minify');
});

gulp.task('watch',function() {
    gulp.watch('./static/css/*.sass', ['sass']);
    gulp.watch('./static/css/*.css', ['minify']);
});
