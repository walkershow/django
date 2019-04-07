let api = {
    v1: {
        task: {
            list: function () {
                return '/api/v1/task/'
            },
            detail: function (id, run = false) {
                let base = `/api/v1/task/${id}/`;
                return run ? base + '?run' : base
            },
        }
    }
}

let store={
    state:{
        list:[],
        id:'',
        name:'',
        output:''
    },
    actions:{
        list:function(){
        $.getJSON({
            url:api.v1.task.list(),
        success:function(data){
            store.state.list = data
        }})
    }
}
}

store.actions.list()



let list ={
    template:`
    <table class = "table table-striped">
    <thead>
    <tr>
    <th class="text-center">文件名</th> 
                <th class="text-center">选项</th> 
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in state.list">
            <td class="text-center">{{ item.task.task_name }}</td>
            <td class="text-center">{{ item.task_group_name }}</td>
            <td>
            </td>
            </tr>
        </tbody> 
    </table>
    `,
    data(){
        return {
            state:store.state
        }
    }
}
let app = { //整体页面布局
    template: `
        <div class="continer-fluid">
            <div class="row text-center h1">
                VM STAT2
            </div>
            <hr>
            <div class="row">
                <div class="col-md-3">
                    <code-list></code-list>
                </div>
            </div>
        </div>
    `,
    components: {
        'code-list': list,
    }
}
let root = new Vue({
    el:'#app',
    template:'<app></app>',
    components:{
    'app':app
    }
})
