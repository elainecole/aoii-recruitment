hk = hk || {};

hk.OutfitView = BB.View.extend({
    el: '#outfit',
    template: _.template($('#outfit-template').html()),

    initialize: function (options) {

        this.model = new BB.Model({
            user: user
        });
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    }
});
