var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var productSchema = new Schema({

  inventory_id: { type: String, Required:  'Product name cannot be left blank.' },

  selling_price:    { type: String,     Required:  'Product price cannot be left blank.'},

  item_category: { type: String ,    Required:  'Product category cannot be left blank'},

  target_audience: { type: String },

  company: { type: String }

});

module.exports = mongoose.model('Products', productSchema);