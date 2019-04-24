let api = {
    v1: {
        task: {
            list: function() {
                return '/api/v1/task/'
            },
            detail: function(id, run = false) {
                let base = `/api/v1/task/${id}/`;
                return run ? base + '?run' : base
            },
        }
    }
}

let store = {
    state: {
        list: [],
        id: '',
        name: '',
        output: ''
    },
    actions: {
        list: function() {
            $.getJSON({
                url: api.v1.task.list(),
                success: function(data) {
                    store.state.list = data
                }
            })
        }
    }
}

store.actions.list()
//setInterval("store.actions.list()", 3000)
let ToggleSwitch = {
    template: `
  <label role="checkbox" :class="['switch', { toggled }]">
    <input type="checkbox" class="switch-input" @change="toggle" />
    <div
      class="switch-core"
      :style="{ backgroundColor: toggled ? colorChecked : colorUnchecked }"
    >
      <div
        class="switch-button"
        }"
      ></div>
    </div>
    <span class="switch-label label-right" v-if="toggled" v-html="labelChecked">
    </span>
    <span class="switch-label label-left" v-html="labelUnchecked" v-else>
    </span>
  </label>
    `,
    data() {
        return {
            toggled: this.value,
            colorChecked: "#25b9e9",
            colorUnchecked: "#db572e",
            labelChecked: "开",
            labelUnchecked: "关"
        };
    },
    props: {
        value: {
            type: Boolean,
            default: true
        },
        speed: {
            type: Number,
            default: 100
        }
    },
    methods: {
        toggle(event) {
            this.toggled = !this.toggled;
            this.$emit("change", event);
        }
    }
}
let list = {
    template: `
    <table class = "table table-striped">
    <thead>
    <tr>
    <th class="text-center">任务组id</th> 
    <th class="text-center">任务id</th> 
    <th class="text-center">任务名</th> 
    <th class="text-center">分配次数</th> 
    <th class="text-center">已成功运行次数</th> 
    <th class="text-center">用户类型</th> 
    <th class="text-center">终端类型</th> 
    <th class="text-center">广告任务</th> 
    <th class="text-center">任务间隔时间</th> 
    <th class="text-center">switcher</th> 
    </tr>
        </thead>
        <tbody>
            <tr v-for="item in state.list">
            <td class="text-center">{{ item.id}}</td>
            <td class="text-center">{{ item.task.id}}</td>
            <td class="text-center">{{ item.task.task_name }}</td>
            <td class="text-center">{{ item.times}}</td>
            <td class="text-center">{{ item.ran_times}}</td>
            <td class="text-center">{{ item.task.get_user_type_display}}</td>
            <td class="text-center">{{ item.task.get_terminal_type_display}}</td>
            <td class="text-center">{{ item.task.get_is_ad_display}}</td>
            <td class="text-center">{{ item.task.inter_time}}</td>
            <td><toggle-switch></toggle-switch></td>

            <td>
            </td>
            </tr>
        </tbody> 
    </table>
    `,
    data() {
        return {
            state: store.state
        }
    },
    components: {
        'toggle-switch': ToggleSwitch
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
        'toggle-switch': ToggleSwitch
    }
}
//let root = new Vue({
//el:'#app',
//template:'<app></app>',
//components:{
//'app':app
//}
//})
//Vue.component("ToggleSwitch", {
Vue.component('tab-home', {
    template: `
        <div class="continer-fluid">
            <div class="row text-center h1">
                VM STAT2
            </div>
            <hr>
            <div class="row">
                <div class="col-md-9">
                    <code-list></code-list>
                </div>
            </div>
        </div>
    `,
    components: {
        'code-list': list,
    }
})

Vue.component('tab-posts', {
    template: `
    <div>
    <transition name ="component-fade" mode="out-in" >

    <component v-bind:is="v-a"></component>
    </transition>
    </div>
    `,
    //components: ['v1', 'v2']
    components: {
        'v-a': {
            template: '<div>Component A</div>'
        },
        'v-b': {
            template: '<div>Component B</div>'
        }
    }
})
Vue.component('tab-archive', {
    template: '<div>Archive component</div>'
})
Vue.component('v1', {
    template: '<h3>hello v1</h3>'
})
Vue.component('v2', {
    template: '<h3>hello v2</h3>'
})
new Vue({
    el: '#dynamic-component-demo',
    data: {
        currentTab: 'Home',
        tabs: ['Home', 'Posts', 'Archive']
    },
    computed: {
        currentTabComponent: function() {
            return 'tab-' + this.currentTab.toLowerCase()
        }
    }
})
