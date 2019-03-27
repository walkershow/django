const api = {
    v1:{
        codes:{
            list:function(){
                return '/vmapi/runningstat'
            },
            validtask:function(){
                return '/vmapi/validtask'
            }
        }
    }
};
let store = {
    list:{
        state:undefined,
        changed:false
    }
}
function getInstance(data){
    let instance = data.fields;
    instance.pk = data.pk
    return instance
}
function getList(){
    $.getJSON({
        url:api.v1.codes.list(),
        success:function(data){
            store.list.state=data.instances;
            store.list.changed=true;
        }
    })
}

function renderToTable(instance, tbody){
    let task = instance;
    let child=`<tr><td class="text-center"><td>${task.server_id}</td>${task.vm_id}</td><td>${task.task_group}</td><td>${task.cur_task_id}</td><td>${task.start_time}</td><td>${task.succ_time}</td><td>${task.status}</td></tr>`;
    tbody.append(child)
}
function watcher(){
    for (let op in store){
        switch(op){
            case 'list':
                if (store[op].changed){
                   let instances = store[op].state;
                    let tbody=$('tbody');
                    tbody.empty();
                    for (let i=0;i<instances.length;i++)
                    { 
                    let instance = getInstance(instances[i])
                        renderToTable(instance, tbody);

                    }
                    store[op].changed=false;

                }
            break;
        }
    }
}
getList();
setInterval("watcher()",500);
setInterval("getList()",700);

