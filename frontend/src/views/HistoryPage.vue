<template>
  <div class="history-page">
    <div class="page-header">
      <h1 class="page-title">检测历史记录</h1>
      <p class="page-subtitle">查看和管理您的所有检测记录</p>
    </div>

    <div class="search-bar">
      <el-input
        v-model="searchQuery"
        placeholder="搜索检测记录..."
        size="default"
        class="search-input"
      >
        <template #prefix>
          <el-icon><Search /></el-icon>
        </template>
      </el-input>

      <el-select v-model="filterStatus" placeholder="状态筛选" size="default" class="filter-select">
        <el-option label="全部" value="" />
        <el-option label="检测完成" value="completed" />
        <el-option label="检测中" value="processing" />
        <el-option label="失败" value="failed" />
      </el-select>

      <el-select v-model="filterType" placeholder="类型筛选" size="default" class="filter-select">
        <el-option label="全部" value="" />
        <el-option label="单图检测" value="single" />
        <el-option label="批量检测" value="batch" />
        <el-option label="视频检测" value="video" />
      </el-select>
    </div>

    <div v-if="filteredRecords.length === 0" class="empty-state">
      <el-icon :size="64" class="empty-icon"><Help /></el-icon>
      <p class="empty-text">暂无检测记录</p>
      <el-button type="primary" @click="$router.push('/detection')">
        <el-icon><Plus /></el-icon>
        开始检测
      </el-button>
    </div>

    <div class="pagination-wrapper" v-if="totalRecords > 0">
      <el-pagination :total="totalRecords" :page-size="10" layout="prev, pager, next" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { Search, Plus, Help } from "@element-plus/icons-vue";

const searchQuery = ref("");
const filterStatus = ref("");
const filterType = ref("");
const historyRecords = ref([]);
const totalRecords = computed(() => historyRecords.value.length);
const filteredRecords = computed(() => historyRecords.value);
</script>

<style scoped>
.history-page { width: 100%; }
.page-header { margin-bottom: 24px; }
.page-title { font-size: 24px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.page-subtitle { font-size: 14px; color: var(--text-secondary); }
.search-bar { display: flex; gap: 12px; margin-bottom: 24px; }
.search-input { max-width: 300px; }
.filter-select { width: 140px; }
.empty-state { display: flex; flex-direction: column; align-items: center; padding: 80px 0; }
.empty-icon { color: var(--success-color); margin-bottom: 16px; }
.empty-text { font-size: 16px; color: var(--text-secondary); margin-bottom: 16px; }
.pagination-wrapper { display: flex; justify-content: center; margin-top: 24px; }
</style>
