// Plugins
const gulp = require('gulp'),
      fs = require('fs');
      concat = require('gulp-concat');
      pjson = require('./package.json'),
      sass = require('gulp-sass'),
      cleancss      = require('gulp-clean-css'),
      autoprefixer = require('gulp-autoprefixer'),
      cssnano = require('gulp-cssnano'),
      rename = require('gulp-rename'),
      del = require('del'),
      plumber = require('gulp-plumber'),
      pixrem = require('gulp-pixrem'),
      uglify = require('gulp-uglify'),
      imagemin = require('gulp-imagemin'),
      exec = require('child_process').exec,
      browserSync = require('browser-sync').create(),
      serverUrl = 'localhost:8000';


function getDirectories(path) {
  return fs.readdirSync(path).filter(function (file) {
    return fs.statSync(`${path}/${file}`).isDirectory() &&
           file !== '__pycache__';
  });
}

// Config
function pathsConfig (appName) {
  const app = `./${appName || pjson.name}`;
  const appsDir = `${app}/apps/`;

  const apps = getDirectories(appsDir)

  const templates = apps.map(function (el) {
    return `${appsDir}${el}/templates/**/*.html`
  });

  console.log(templates)

  return {
    app: app,
    env: 'venv',
    templates: [
      `${app}/templates/**/*.html`,
      ...templates
    ],
    sass: `${app}/static/sass/**/*.sass`,
    fonts: `${app}/static/fonts/**/*`,
    images: `${app}/static/images/**/*`,
    libs: [
      `${app}/static/libs/**/*.js`,
    ],
    js: `${app}/static/js/**/*.js`,
    dist: `${app}/static/dist`,
  }
};

const paths = pathsConfig();


// Styles
gulp.task('styles', function() {
  return gulp.src(paths.sass)
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber())
    .pipe(autoprefixer())
    .pipe(cleancss( {level: { 1: { specialComments: 0 } } }))
    .pipe(pixrem())
    .pipe(cssnano())
    .pipe(gulp.dest(`${paths.dist}/css`))
    .pipe(browserSync.stream());
});


// Scripts
gulp.task('scripts', function() {
  return gulp.src(paths.js)
    .pipe(plumber())
    .pipe(uglify())
    .pipe(concat('script.js'))
    .pipe(gulp.dest(`${paths.dist}/js`))
    .pipe(browserSync.reload({ stream: true }));
});


// Libs
gulp.task('libs', function() {
  return gulp.src(paths.libs)
    .pipe(concat('vendor.js'))
    .pipe(gulp.dest(`${paths.dist}/js`))
    .pipe(browserSync.reload({ stream: true }));
});


// Fonts
gulp.task('fonts', function() {
  return gulp.src(paths.fonts)
    .pipe(gulp.dest(`${paths.dist}/fonts`));
});


// Templates
gulp.task('templates', function() {
  return gulp.src(paths.templates)
    .pipe(browserSync.reload({ stream: true }))
});


// Images
gulp.task('imgCompression', function(){
  return gulp.src(paths.images)
    .pipe(imagemin())
    .pipe(gulp.dest(`${paths.dist}/images`))
});


// Run django server
gulp.task('runServer', function(cb) {
  var isWin = /^win/.test(process.platform);
  var cmd =  `source ${paths.env}/bin/activate && PYTHONUNBUFFERED=1 && `;

  if (isWin) {
    cmd = `${paths.env}\\Scripts\\activate.bat && set PYTHONUNBUFFERED=1 && `;
  }

  var proc = exec(cmd + `python ./${pjson.name}/manage.py runserver ${serverUrl}`);
  proc.stderr.on('data', function(data) {
    process.stdout.write(data);
  });

  proc.stdout.on('data', function(data) {
    process.stdout.write(data);
  });
});


// Browser sync server for live reload
gulp.task('browserSync', function() {
    browserSync.init(
      [paths.sass, paths.js, paths.templates], {
        proxy:  serverUrl,
        port: 8080,
        reloadDelay: 300,
        reloadDebounce: 500
    });
});


// Watch
gulp.task('watch', function() {
  gulp.watch(paths.libs, gulp.parallel('libs'));
  gulp.watch(paths.sass, gulp.parallel('styles'));
  gulp.watch(paths.js, gulp.parallel('scripts'))
  gulp.watch(paths.images, gulp.parallel('imgCompression'));
  gulp.watch(paths.templates, gulp.parallel('templates'));
  gulp.watch(paths.fonts, gulp.parallel('fonts'));
});


// Default task
gulp.task('default', gulp.parallel(
  'libs', 'fonts', 'styles',
  'scripts', 'imgCompression',
  'runServer', 'browserSync', 'watch'
));
