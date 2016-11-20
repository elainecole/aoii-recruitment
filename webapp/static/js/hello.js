hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),
    userTemplate: _.template($('#user-template').html()),

    initialize: function (options) {

        this.model = new hk.HelloUserModel();
        this.render();

        this.listenTo(this.model, 'sync', this.renderUser)
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    renderUser: function () {
        this.$('.user-holder').empty().append(this.userTemplate());
    }
});
