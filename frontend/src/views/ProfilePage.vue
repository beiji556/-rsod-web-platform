<template>
  <div class="profile-page">
    <div class="page-header">
      <h1 class="page-title">个人中心</h1>
    </div>

    <div class="profile-card">
      <div class="profile-avatar">
        <el-avatar :size="80">
          <img src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" alt="头像" />
        </el-avatar>
        <div class="profile-name">Lily</div>
        <div class="profile-role">普通用户</div>
      </div>

      <div class="profile-stats">
        <div class="stat-item">
          <div class="stat-value">0</div>
          <div class="stat-label">检测次数</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">0</div>
          <div class="stat-label">检测目标</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">10</div>
          <div class="stat-label">目标类别</div>
        </div>
      </div>
    </div>

    <div class="menu-card">
      <div class="menu-item" v-for="item in menuItems" :key="item.label">
        <el-icon><component :is="item.icon" /></el-icon>
        <span>{{ item.label }}</span>
        <el-icon class="arrow"><ArrowRight /></el-icon>
      </div>
    </div>

    <div class="logout-section">
      <el-button type="danger" size="large" class="logout-btn" @click="handleLogout">
        退出登录
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { User, Setting, InfoFilled, ArrowRight } from "@element-plus/icons-vue";

const router = useRouter();

const menuItems = [
  { label: "个人信息", icon: User },
  { label: "系统设置", icon: Setting },
  { label: "关于平台", icon: InfoFilled },
];

const handleLogout = () => {
  localStorage.removeItem("token");
  router.push("/login");
};
</script>

<style scoped>
.profile-page { width: 100%; max-width: 600px; }
.page-header { margin-bottom: 24px; }
.page-title { font-size: 24px; font-weight: 600; color: var(--text-primary); }
.profile-card { background: #fff; border-radius: 12px; padding: 32px; text-align: center; margin-bottom: 16px; }
.profile-avatar { margin-bottom: 24px; }
.profile-name { font-size: 18px; font-weight: 600; color: var(--text-primary); margin-top: 12px; }
.profile-role { font-size: 13px; color: var(--text-secondary); margin-top: 4px; }
.profile-stats { display: flex; justify-content: center; gap: 48px; }
.stat-value { font-size: 24px; font-weight: 700; color: var(--primary-color); }
.stat-label { font-size: 13px; color: var(--text-secondary); margin-top: 4px; }
.menu-card { background: #fff; border-radius: 12px; margin-bottom: 16px; }
.menu-item { display: flex; align-items: center; padding: 16px 20px; cursor: pointer; transition: background 0.2s; }
.menu-item:hover { background: #f9fafb; }
.menu-item span { flex: 1; margin-left: 12px; font-size: 14px; color: var(--text-primary); }
.arrow { font-size: 14px; color: var(--text-secondary); }
.logout-section { text-align: center; }
.logout-btn { width: 100%; height: 44px; border-radius: 8px; }
</style>
