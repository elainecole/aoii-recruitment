hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),
    userTemplate: _.template($('#user-template').html()),

    initialize: function (options) {

        this.model = new BB.Model({
            user: user
        });
        this.render();

        // this.listenTo(this.model, 'sync', this.renderUser)
    },

    render: function () {
        this.$el.empty().append(this.template());
        console.log(this.$('.user-holder'));
        this.$('.user-holder').empty().append(this.userTemplate());

    }
});
