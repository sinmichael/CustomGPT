import { Injectable } from '@nestjs/common';
import Redis from 'ioredis';
import { v4 as uuidv4 } from 'uuid';

@Injectable()
export class RedisService {
  private readonly redisClient: Redis;

  constructor() {
    this.redisClient = new Redis({ host: process.env.REDIS_HOST });
  }

  async publishAndWait(message) {
    const requestChannel = `request-channel:${uuidv4()}`;

    this.redisClient.publish(
      'request-channel',
      JSON.stringify({
        channel: requestChannel,
        message,
      }),
    );

    this.redisClient.subscribe(requestChannel);

    return new Promise((resolve) => {
      this.redisClient.on('message', (channel, reply) => {
        this.redisClient.unsubscribe(requestChannel);
        resolve(JSON.parse(reply));
      });
    });
  }
}
