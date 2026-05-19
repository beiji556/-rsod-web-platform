<template>
  <div class="targets-page">
    <div class="page-header">
      <h1 class="page-title">目标类别库</h1>
      <p class="page-subtitle">查看系统支持检测的所有遥感目标类别</p>
    </div>

    <div class="target-grid">
      <div v-for="target in targets" :key="target.id" class="target-card">
        <div class="target-color" :style="{ backgroundColor: target.color }"></div>
        <div class="target-info">
          <span class="target-name">{{ target.name }}</span>
          <span class="target-chinese">{{ target.chinese_name }}</span>
          <span class="target-desc">{{ target.description || '暂无描述' }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const targets = ref([
  { id: 1, name: "airplane", chinese_name: "飞机", description: "固定翼飞机、直升机等", color: "#ef4444" },
  { id: 2, name: "oil_tank", chinese_name: "油罐", description: "储油罐、化工罐等", color: "#f59e0b" },
  { id: 3, name: "playground", chinese_name: "操场", description: "运动场、操场等", color: "#10b981" },
  { id: 4, name: "building", chinese_name: "建筑物", description: "各类建筑物", color: "#3b82f6" },
  { id: 5, name: "ship", chinese_name: "船舶", description: "各类船舶", color: "#8b5cf6" },
  { id: 6, name: "pest", chinese_name: "农业虫害", description: "农作物病虫害", color: "#ec4899" },
  { id: 7, name: "person", chinese_name: "行人", description: "人体目标", color: "#06b6d4" },
  { id: 8, name: "car", chinese_name: "汽车", description: "各类汽车", color: "#84cc16" },
  { id: 9, name: "bus", chinese_name: "公交车", description: "公共汽车", color: "#f97316" },
  { id: 10, name: "truck", chinese_name: "卡车", description: "货运卡车", color: "#6366f1" },
]);
</script>

<style scoped>
.targets-page { width: 100%; }
.page-header { margin-bottom: 24px; }
.page-title { font-size: 24px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.page-subtitle { font-size: 14px; color: var(--text-secondary); }
.target-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
.target-card { display: flex; align-items: center; gap: 16px; padding: 20px; background: #fff; border-radius: 12px; transition: box-shadow 0.2s; }
.target-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.target-color { width: 48px; height: 48px; border-radius: 10px; flex-shrink: 0; }
.target-info { display: flex; flex-direction: column; gap: 4px; }
.target-name { font-size: 14px; font-weight: 600; color: var(--text-primary); }
.target-chinese { font-size: 13px; color: var(--text-secondary); }
.target-desc { font-size: 12px; color: #9ca3af; }
</style>
