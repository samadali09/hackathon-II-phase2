'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { authClient } from '@/lib/auth-client';
import { taskApi } from '@/lib/api';
import { useTheme } from '@/contexts/ThemeContext';

interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTaskTitle, setNewTaskTitle] = useState('');
  const [newTaskDescription, setNewTaskDescription] = useState('');
  const [filter, setFilter] = useState<'all' | 'pending' | 'completed'>('all');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const router = useRouter();
  const { theme, toggleTheme } = useTheme();

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await taskApi.getTasks();
      setTasks(data);
      setError('');
    } catch (err) {
      console.error('Failed to load tasks:', err);
      setError('Failed to load tasks');
    } finally {
      setLoading(false);
    }
  };

  const filteredTasks = tasks
    .filter((task) => {
      if (searchQuery) {
        return task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
               (task.description && task.description.toLowerCase().includes(searchQuery.toLowerCase()));
      }
      return true;
    })
    .filter((task) => {
      if (filter === 'pending') return !task.completed;
      if (filter === 'completed') return task.completed;
      return true;
    });

  const handleAddTask = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTaskTitle.trim()) return;

    try {
      const newTask = await taskApi.createTask(newTaskTitle, newTaskDescription);
      setTasks([...tasks, newTask]);
      setNewTaskTitle('');
      setNewTaskDescription('');
      setError('');
    } catch (err) {
      console.error('Failed to create task:', err);
      setError('Failed to create task');
    }
  };

  const handleToggleTask = async (id: number, completed: boolean) => {
    try {
      const updatedTask = await taskApi.toggleComplete(id, !completed);
      setTasks(tasks.map((task) => (task.id === id ? updatedTask : task)));
      setError('');
    } catch (err) {
      console.error('Failed to toggle task:', err);
      setError('Failed to update task');
    }
  };

  const handleDeleteTask = async (id: number) => {
    try {
      await taskApi.deleteTask(id);
      setTasks(tasks.filter((task) => task.id !== id));
      setError('');
    } catch (err) {
      console.error('Failed to delete task:', err);
      setError('Failed to delete task');
    }
  };

  const handleSignOut = async () => {
    try {
      await authClient.signOut();
      router.push('/');
    } catch (err) {
      console.error('Failed to sign out:', err);
    }
  };

  const taskStats = {
    total: tasks.length,
    completed: tasks.filter(t => t.completed).length,
    pending: tasks.filter(t => !t.completed).length
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-3xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="flex items-center justify-center w-10 h-10 bg-blue-600 rounded-lg">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                </svg>
              </div>
              <h1 className="text-xl font-bold text-gray-900">TaskFlow</h1>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={toggleTheme}
                className="p-2 rounded-lg hover:bg-gray-100 text-gray-600 transition-colors"
                aria-label="Toggle theme"
              >
                {theme === 'dark' ? '☀️' : '🌙'}
              </button>
              <button
                onClick={handleSignOut}
                className="px-4 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
              >
                Sign Out
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-3xl mx-auto px-4 py-8">
        {/* Stats */}
        <div className="grid grid-cols-3 gap-4 mb-6">
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <p className="text-xs text-gray-500 uppercase font-medium">Total</p>
            <p className="text-2xl font-bold text-gray-900">{taskStats.total}</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <p className="text-xs text-gray-500 uppercase font-medium">Completed</p>
            <p className="text-2xl font-bold text-green-600">{taskStats.completed}</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-sm">
            <p className="text-xs text-gray-500 uppercase font-medium">Pending</p>
            <p className="text-2xl font-bold text-blue-600">{taskStats.pending}</p>
          </div>
        </div>

        {/* Add Task */}
        <form onSubmit={handleAddTask} className="bg-white rounded-lg p-4 shadow-sm mb-6">
          <div className="flex gap-3">
            <input
              type="text"
              value={newTaskTitle}
              onChange={(e) => setNewTaskTitle(e.target.value)}
              placeholder="Add a new task..."
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
            <button
              type="submit"
              disabled={!newTaskTitle.trim() || loading}
              className="px-6 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Add
            </button>
          </div>
          {newTaskTitle && (
            <input
              type="text"
              value={newTaskDescription}
              onChange={(e) => setNewTaskDescription(e.target.value)}
              placeholder="Description (optional)"
              className="w-full mt-3 px-4 py-2 border border-gray-300 rounded-lg text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          )}
        </form>

        {/* Search & Filter */}
        <div className="flex flex-col sm:flex-row gap-3 mb-4">
          <div className="flex-1">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search tasks..."
              className="w-full px-4 py-2 border border-gray-300 rounded-lg text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <div className="flex gap-2">
            {(['all', 'pending', 'completed'] as const).map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`px-4 py-2 text-sm font-medium rounded-lg capitalize transition-colors ${
                  filter === f
                    ? 'bg-blue-600 text-white'
                    : 'bg-white text-gray-600 hover:bg-gray-50'
                }`}
              >
                {f}
              </button>
            ))}
          </div>
        </div>

        {/* Error */}
        {error && (
          <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-600 text-sm rounded-lg">
            {error}
          </div>
        )}

        {/* Task List */}
        {loading ? (
          <div className="text-center py-12">
            <div className="animate-spin h-8 w-8 border-4 border-blue-600 border-t-transparent rounded-full mx-auto mb-4"></div>
            <p className="text-gray-600">Loading tasks...</p>
          </div>
        ) : filteredTasks.length === 0 ? (
          <div className="bg-white rounded-lg p-12 shadow-sm text-center">
            <div className="w-16 h-16 mx-auto mb-4 bg-gray-100 rounded-full flex items-center justify-center">
              <svg className="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-1">
              {filter === 'all' && 'No tasks yet'}
              {filter === 'pending' && 'No pending tasks'}
              {filter === 'completed' && 'No completed tasks'}
            </h3>
            <p className="text-sm text-gray-500">
              {filter === 'all' && 'Add your first task above'}
              {filter === 'pending' && 'All caught up!'}
              {filter === 'completed' && 'Complete some tasks to see them here'}
            </p>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-sm divide-y divide-gray-100">
            {filteredTasks.map((task) => (
              <div
                key={task.id}
                className="flex items-start gap-4 p-4 hover:bg-gray-50 transition-colors group"
              >
                <button
                  onClick={() => handleToggleTask(task.id, task.completed)}
                  className={`flex-shrink-0 w-6 h-6 mt-0.5 rounded border-2 flex items-center justify-center transition-colors ${
                    task.completed
                      ? 'bg-green-500 border-green-500'
                      : 'border-gray-300 hover:border-blue-500'
                  }`}
                >
                  {task.completed && (
                    <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                </button>
                <div className="flex-1 min-w-0">
                  <h3 className={`font-medium text-gray-900 break-words ${
                    task.completed ? 'line-through text-gray-500' : ''
                  }`}>
                    {task.title}
                  </h3>
                  {task.description && (
                    <p className="text-sm text-gray-500 mt-1 break-words">{task.description}</p>
                  )}
                  <p className="text-xs text-gray-400 mt-2">
                    {new Date(task.created_at).toLocaleDateString()}
                  </p>
                </div>
                <button
                  onClick={() => handleDeleteTask(task.id)}
                  className="flex-shrink-0 p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors opacity-0 group-hover:opacity-100"
                  aria-label="Delete task"
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
