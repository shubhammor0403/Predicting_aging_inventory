var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var productSchema = new Schema({

  inventory_id: { type: String },

  inventory_location: { type: String },

  itemid: { type: String },

  item_category: { type: String },

  company: { type: String },

  no_items_recieved: { type: String },

  no_items_remaining: { type: String},

  date_recieved: { type: String },

  no_of_days: { type: String },

  currently_in_inventory: { type: String },

  date_sent: { type: String },

  inventory_sent: { type: String }

});

module.exports = mongoose.model('Products', productSchema);