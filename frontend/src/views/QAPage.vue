<template>
  <div class="qa-page">
    <div class="page-header">
      <h1 class="page-title">AI 智能问答</h1>
      <p class="page-subtitle">基于遥感检测结果的智能分析与建议</p>
    </div>

    <div class="chat-container">
      <div class="chat-messages" ref="chatRef">
        <div v-for="(msg, index) in messages" :key="index" class="message" :class="msg.role">
          <div class="message-avatar">
            <el-icon :size="24"><component :is="msg.role === 'user' ? User : ChatDotRound" /></el-icon>
          </div>
          <div class="message-content">{{ msg.content }}</div>
        </div>
      </div>

      <div class="chat-input">
        <el-input
          v-model="question"
          placeholder="请输入您的问题..."
          size="large"
          @keyup.enter="handleSend"
        >
          <template #append>
            <el-button type="primary" @click="handleSend" :disabled="!question.trim()">
              发送
            </el-button>
          </template>
        </el-input>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from "vue";
import { User, ChatDotRound } from "@element-plus/icons-vue";

const question = ref("");
const messages = ref([
  { role: "assistant", content: "您好！我是遥感检测AI助手，可以帮您分析检测结果、解答技术问题。" },
]);
const chatRef = ref(null);

const handleSend = () => {
  if (!question.value.trim()) return;
  messages.value.push({ role: "user", content: question.value });
  question.value = "";
  setTimeout(() => {
    messages.value.push({ role: "assistant", content: "这是一个模拟回复。AI问答功能将在后续版本中实现。" });
    nextTick(() => {
      if (chatRef.value) chatRef.value.scrollTop = chatRef.value.scrollHeight;
    });
  }, 500);
  nextTick(() => {
    if (chatRef.value) chatRef.value.scrollTop = chatRef.value.scrollHeight;
  });
};
</script>

<style scoped>
.qa-page { width: 100%; height: calc(100vh - 160px); display: flex; flex-direction: column; }
.page-header { margin-bottom: 24px; flex-shrink: 0; }
.page-title { font-size: 24px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.page-subtitle { font-size: 14px; color: var(--text-secondary); }
.chat-container { flex: 1; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; }
.chat-messages { flex: 1; overflow-y: auto; padding: 24px; display: flex; flex-direction: column; gap: 16px; }
.message { display: flex; gap: 12px; }
.message.user { flex-direction: row-reverse; }
.message-avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--primary-light); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.message-content { max-width: 70%; padding: 12px 16px; border-radius: 12px; font-size: 14px; line-height: 1.6; }
.message.assistant .message-content { background: #f3f4f6; color: var(--text-primary); }
.message.user .message-content { background: var(--primary-color); color: #fff; }
.chat-input { padding: 16px 24px; border-top: 1px solid var(--border-color); }
</style>
