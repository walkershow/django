<template>
  <table class="table table-striped">
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
        <th class="text-center">开关</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in list" :key="index">
        <td class="text-center">{{ item.id }}</td>
        <td class="text-center">{{ item.task.id }}</td>
        <td class="text-center">{{ item.task.task_name }}</td>
        <td class="text-center">{{ item.times }}</td>
        <td class="text-center">{{ item.ran_times }}</td>
        <td class="text-center">{{ item.task.get_user_type_display }}</td>
        <td class="text-center">{{ item.task.get_terminal_type_display }}</td>
        <td class="text-center">{{ item.task.get_is_ad_display }}</td>
        <td class="text-center">{{ item.task.inter_time }}</td>
        <td>
          <toggle-switch
            :value="Boolean(item.task.status)"
            v-bind:task="item"
          ></toggle-switch>
        </td>

        <td></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import ToggleSwitch from "./tswitch.vue";
import axios from "axios";
export default {
  name: "codelist",
  data() {
    return {
      list: null
    };
  },
  mounted() {
    axios
      .get("http://192.168.1.166:8000/api/v1/task/")
      .then(response => (this.list = response.data));
  },
  components: {
    "toggle-switch": ToggleSwitch
  }
};
</script>
