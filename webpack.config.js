const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const CleanWebpackPlugin = require('clean-webpack-plugin');



module.exports = {
  // the base directry (absolute path) for resolving the entry option
  context: __dirname,

  // the entry point we created earlier. Note that './' means
  // your current directory. You don't have to specify the extension now,
  // because you will specify extensions later in the `resolve` section
  entry: {
    main: './assets/app/index.js',
    scripts: './assets/scripts/index.js',
    particles: './assets/scripts/threejs/index.js'
  },

  output: {
    // where you want your compiled bundle to be stored
    path: path.resolve('./home/static/bundles/'),
    filename: '[name].bundle.js',
  },

  plugins: [
    // telss webpack where to store data about your bundles
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin("[name].styles.css"),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }),
    new CleanWebpackPlugin(
      ['./home/static/bundles/'],
      { root: process.cwd() }
    ),
  ],

  module: {
    loaders: [
      // a regexp that tells webpack to use the following loads on all .js and .jsx files
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          // specify that we will be dealing with React code
          presets: ['react']
        }
      },
      // LESS to CSS
      {
        test: /\.less$/,
        loader: ExtractTextPlugin.extract([ 'css-loader', 'less-loader' ])
      },
      // CSS
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      // JSON
      {
        test: /\.json$/,
        use: [ 'json-loader' ]
      },
      // IMAGES
      {
        test: /\.(png|svg|jpg|gif)$/,
        loader: ['file-loader']
      },
      // FONTS
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader'
        ]
      }

    ]
  },
  watchOptions: {
    aggregateTimeout: 100,
    ignored: /node_modules/,
    poll: 1000
  },

  resolve: {
    // tells webpack where to look for modules
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
}
